from django.contrib import admin
from .models import Game, Tag, Media, SystemRequirements, Profile

admin.site.register(Profile)
admin.site.register(Game)
admin.site.register(Tag)
admin.site.register(Media)
admin.site.register(SystemRequirements)
