from django.contrib import admin

from geolocation.models import Room, UserInfo, Location

# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'active', 'created']


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'room', 'device', 'created']


class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'user_info', 'latitude', 'longitude', 'direction', 'created']



admin.site.register(Room, RoomAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Location, LocationAdmin)