from django.contrib import admin
from .models import *


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ["name", "gender", 'element', 'height', 'hair']

@admin.register(Move)
class MoveAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "owner"]

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ["number", "name"]

@admin.register(Timeline)
class TimelineAdmin(admin.ModelAdmin):
    list_display = ["date_field", "event"]

@admin.register(Sight)
class SightAdmin(admin.ModelAdmin):
    list_display = ["name", "first_seen", 'description']

@admin.register(Outfit)
class OutfitAdmin(admin.ModelAdmin):
    list_display = ["name", "worn_by", 'description']
