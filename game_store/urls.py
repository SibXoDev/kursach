"""game_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store import views as store_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', store_views.view),
    path('store/<str:game_id>/', store_views.view_game),
    path('auth/', store_views.view_auth),
    path('register/', store_views.view_register),
    path('logout/', store_views.view_logout),
    path('library/', store_views.view_library),
    path('category/create/', store_views.view_category),
    path('game/create/', store_views.view_game_create),
    path('game/edit/<int:game_id>/', store_views.view_game_edit),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)