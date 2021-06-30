from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class UserSerializerWithToken(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, user):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password', 'email')

class ExtendedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendedUser
        fields = ('id', 'user', 'profilepic')

class DisplayTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisplayType
        fields = ('id', 'name')

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
    timeline = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='title'
    )
    class Meta:
        model = Entry
        fields = ['id', 'user', 'timeline', 'title', 'categories', 'datetime', 'summary', 'description', 'image']

class TimelineSerializer(serializers.ModelSerializer):
    entries = EntrySerializer(many=True, read_only=True)
    class Meta:
        model = Timeline
        fields = ('id', 'user', 'title', 'private', 'entries')
