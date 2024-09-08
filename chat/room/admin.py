from django.contrib import admin
from .models import Room, Message




@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'is_active']
    prepopulated_fields = {'slug':('name',)}



@admin.register(Message)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['content', 'date_added', 'is_active']
