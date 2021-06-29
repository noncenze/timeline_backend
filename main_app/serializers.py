from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class ExtendedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendedUser
        fields = ('id', 'user', 'profilepic')

class DisplayTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisplayType
        fields = ('id', 'name')

class TimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeline
        fields = ('id', 'user', 'title', 'private')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'primary', 'timeline', 'displaytype')

class EntrySerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    class Meta:
        model = Entry
        fields = ('id', 'user', 'timeline', 'title', 'categories', 'datetime', 'summary', 'description', 'image')
