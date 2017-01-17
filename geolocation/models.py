from __future__ import unicode_literals

from django.db import models

from common import mixins

# Create your models here.

class Room(mixins.UneditableMixin):
    name = models.CharField(max_length=20)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class Device(mixins.UneditableMixin):
    os     = models.CharField(max_length=50, verbose_name='Device OS')
    name   = models.CharField(max_length=200, blank=True, null=True,
                              verbose_name='Device Model')
    reg_id = models.TextField(verbose_name='Registration ID',
                              unique=True, blank=True, null=True)
    version= models.CharField(max_length=50, blank=True, null=True,
                              verbose_name='App Version')
    active = models.BooleanField(default=True)
    extra  = models.TextField(blank=True, null=True,
                help_text="Stringified dict. Like 'installed app name'")

    def __unicode__(self):
        return self.name


class RoomUser(mixins.UneditableMixin):
    name = models.CharField(max_length=100, blank=True, null=True)
    room = models.ForeignKey(Room)
    device = models.ForeignKey(Device, related_name='room_user')

    def __unicode__(self):
        return self.name


class Location(mixins.UneditableMixin):
    name = models.CharField(max_length=100, blank=True, null=True)
    room_user = models.ForeignKey(RoomUser, related_name='locations')
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    extra = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name