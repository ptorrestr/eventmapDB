from django.db import models
from djangotoolbox.fields import  EmbeddedModelField, ListField

class Event(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    name = models.CharField(unique = True, max_length = 1024)
    address = models.CharField(max_length = 1024)
    gmaps = models.BooleanField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    alert = models.IntegerField()

class Tweet(models.Model):
    #Foreign Key
    event = models.ForeignKey(Event, related_name = 'tweets')
    #Fields
    created_at = models.DateTimeField(auto_now_add = True)
    twitter_id = models.BigIntegerField(unique = True)
    twitter_text = models.CharField(max_length = 200)
    twitter_user_id = models.BigIntegerField()
    twitter_screen_name = models.CharField(max_length = 200)
    twitter_profile_image_url = models.CharField(max_length = 1024)

class Image(models.Model):
    #Foreign Key
    event = models.ForeignKey(Event, related_name = 'images')
    #Fields
    created_at = models.DateTimeField(auto_now_add = True)
    url = models.CharField(max_length = 1024)

class Video(models.Model):
    #Foreign Key
    event = models.ForeignKey(Event, related_name = 'videos')
    #Fields
    created_at = models.DateTimeField(auto_now_add = True)
    url = models.CharField(max_length = 1024)
