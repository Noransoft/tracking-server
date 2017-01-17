from django.contrib import admin

from geolocation.models import Room, RoomUser, Location, Device

# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'active', 'created']


class DeviceAdmin(admin.ModelAdmin):
    list_display = ['os', 'name', 'version', 'active', 'created']


class RoomUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'room', 'device', 'created']


class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'room_user', 'latitude', 'longitude', 'created']



admin.site.register(Room, RoomAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(RoomUser, RoomUserAdmin)
admin.site.register(Location, LocationAdmin)