from __future__ import unicode_literals

from django.db import models

from common import mixins

# Create your models here.

class Room(mixins.UneditableMixin):
    name = models.CharField(max_length=500)
    unique_id = models.CharField(max_length=500)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class UserInfo(mixins.UneditableMixin):
    name = models.CharField(max_length=500)
    room = models.ForeignKey(Room)
    device = models.CharField(max_length=500)
    extra = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Location(mixins.UneditableMixin):
    name = models.CharField(max_length=500)
    user_info = models.ForeignKey(UserInfo)
    latitude = models.FloatField()
    longitude = models.FloatField()
    direction = models.CharField(max_length=500)
    extra = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name