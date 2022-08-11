from dataclasses import field
from rest_framework import serializers
from .models import Auth

# 220810
from .models import PostInfo

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auth
        fields = ('nickname','uid','password')

# 220810
class PostInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostInfo
        fields = ('title', 'description', 'category')

# 220810
class PostInfoDetailSerilizer(serializers.ModelSerializer):
    class Meta:
        model = PostInfo
        fields = ('title', 'description', 'author', 'category')