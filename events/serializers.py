from rest_framework import serializers
from events.models import Event
from events.models import Tweet
from events.models import Video
from events.models import Image

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('twitter_id',
                'twitter_text',
                'twitter_user_id',
                'twitter_screen_name',
                'twitter_profile_image_url',)

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('url',)

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('url',)

class EventSerializer(serializers.ModelSerializer):
    tweets = TweetSerializer(many = True, required = False)
    images = ImageSerializer(many = True, required = False)
    videos = VideoSerializer(many = True, required = False)

    class Meta:
        model = Event
        fields = ('id', 
                'name',
                'address',
                'gmaps',
                'latitude',
                'longitude',
                'alert',
                'tweets',
                'images',
                'videos')
