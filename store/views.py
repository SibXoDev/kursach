from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from django.http import JsonResponse, HttpResponseNotFound, Http404
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from game_store.forms import CustomUserCreationForm
from .forms import GameCreationForm, SysReqCreationForm
from .models import Game, Tag, Media, SystemRequirements, Profile

sys_req_names = {
    "os": "ОС",
    "cpu": "Процессор",
    "ram": "Оперативная память",
    "disk_space": "Место на диске",
    "gpu": "Видеокарта"
}

sys_req_measure = {
    "ram": "ГБ",
    "disk_space": "ГБ",
}

# @login_required
def view_auth(request):
    if request.method == "GET":
        if request.GET.get("check"):
            return JsonResponse({"auth": request.user.is_authenticated})

    if not request.user.is_authenticated:
        if request.method == "POST":
            response_data = {
                "auth": False
            }
            
            user = authenticate(request, username=request.POST.get("username", ""), password=request.POST.get("password", ""))

            if user is not None:
                if user.is_active:
                    login(request, user)
                    response_data["auth"] = True
                else:
                    response_data["message"] = "Пользователь больше не действителен!"
            else:
                response_data["message"] = "Пароль или логин введены неправильно!"

            return JsonResponse(response_data)
        return render(request, "auth.html")
    return redirect("/")

def view_register(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)

            response_data = {
                "auth": form.is_valid()
            }

            if form.is_valid():
                user = form.save()
                login(request, user)
            else:
                response_data["message"] = form.errors
    
            return JsonResponse(response_data)
    return redirect("/")

def view_logout(request):
    logout(request)
    if request.method == "GET":
        return redirect(request.GET.get("next", "/"))
    return redirect("/")

def view(request):
    context = {
        "games": Game.objects.all().order_by("name"),
        "user_games": [],
        "favorites_games": []
    }

    if request.user.is_authenticated:
        context["favorites_games"] = request.user.profile.favorites.all().order_by("name")
        context["user_games"] = request.user.profile.games.all().order_by("name")

    if request.method == "GET":
        if request.GET.get("search", False):
            context["games"] = Game.objects.filter(name__iregex = fr'{request.GET["search"]}').order_by("name")
            if request.user.is_authenticated:
                context["favorites_games"] = request.user.profile.favorites.filter(name__iregex = fr'{request.GET["search"]}').order_by("name")
                context["user_games"] = request.user.profile.games.filter(name__iregex = fr'{request.GET["search"]}').order_by("name")

    return render(request, "index.html", context)

@csrf_protect
def view_game(request, game_name):
    game = get_if_exists(Game, name = game_name)
    context = {
        "game": game,
        "acquired": False,
        "favorites": False
    }

    if request.user.is_authenticated and game:
        if request.method == "POST":
            if not request.user.profile.games.filter(pk=game.id).exists():
                if request.POST.get("buy", False):
                    request.user.profile.games.add(game)
                    request.user.profile.favorites.remove(game)
                    return JsonResponse({"add": True})
                elif request.POST.get("favorites", False):
                    if request.user.profile.favorites.filter(pk=game.id).exists():
                        request.user.profile.favorites.remove(game)
                        return JsonResponse({"add": False})
                    else:
                        request.user.profile.favorites.add(game)
                        return JsonResponse({"add": True})
            return JsonResponse({})
        
        context["acquired"] = request.user.profile.games.filter(pk=game.id).exists()
        context["favorites"] = request.user.profile.favorites.filter(pk=game.id).exists()

    if game:
        context["sys_req"] = [[sys_req_names[field.name], getattr(game.sys_req, field.name), sys_req_measure.get(field.name, "")] for field in game.sys_req._meta.get_fields() if field.name in sys_req_names]

    return render(request, "game.html", context)

def view_library(request):
    if request.user.is_authenticated:
        context = {
            "games": request.user.profile.games.all().order_by("name"),
            "search": False
        }

        if request.method == "GET":
            if request.GET.get("search", False):
                context["search"] = True
                context["games"] = Game.objects.filter(name__iregex = fr'{request.GET["search"]}').order_by("name")

        return render(request, "library.html", context)
    return redirect("/auth?next=/library/")

def view_game_create(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            form_sys_req = SysReqCreationForm(request.POST)
            if form_sys_req.is_valid():
                sys_req = form_sys_req.save()
                data = request.POST.copy()
                data["sys_req"] = sys_req
                form_game = GameCreationForm(data, request.FILES)
                if form_game.is_valid():
                    form_game.save()
                    return JsonResponse({"add": True})
                else:
                    sys_req.delete()
            return JsonResponse({"add": False})
        return render(request, "game_create.html")
    raise Http404

def view_game_edit(request, game_id):
    if request.user.is_authenticated and request.user.is_superuser and game_id >= 0:
        instance_game = get_object_or_404(Game, pk = game_id)
        instance_sys_req = get_object_or_404(SystemRequirements, pk = instance_game.sys_req.id)

        data = request.POST.copy()
        data["sys_req"] = instance_game.sys_req.id

        if request.method == "POST":
            form_game = GameCreationForm(data, request.FILES, instance = instance_game)
            form_sys_req = SysReqCreationForm(data, instance = instance_sys_req)

            if form_game.is_valid() and form_sys_req.is_valid():
                update_fields = []
                for field in data:
                    if data[field] != "csrfmiddlewaretoken" and data[field]:
                        update_fields.append(field)

                form_game.save(update_fields)
                form_sys_req.save(update_fields)

                return JsonResponse({"edit": True, "img_url": Game.objects.get(pk = game_id).preview.url})
            return JsonResponse({"edit": False})
        return render(request, "game_edit.html", {"game": instance_game, "sys_req": instance_sys_req})
    raise Http404

def get_if_exists(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None