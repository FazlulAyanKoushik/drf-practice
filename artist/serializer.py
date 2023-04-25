"""
    Serializer for Artist model
"""
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Artist

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ArtistSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Artist
        fields = ["id", "user", "name", "age"]
        # read_only_fields = ["id", "name"]

    def create(self, validated_data):
        artist = Artist.objects.create(**validated_data)
        return artist

    def update(self, instance, validated_data):
        instance.age = validated_data.get("age", instance.age)
        instance.save()
        return instance
