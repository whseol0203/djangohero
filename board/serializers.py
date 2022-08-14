from dataclasses import field
from rest_framework import serializers
from .models import Auth, Comment

# 220810
from .models import PostInfo

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auth
        fields = ('nickname','uid','password')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('nickname','contents','commentUser')



# 220810
class PostInfoListSerializer(serializers.ModelSerializer):
    postInfo = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = PostInfo
        fields = ('title', 'category', 'postInfo','postUser')

# 220810
class PostInfoDetailSerilizer(serializers.ModelSerializer):
    class Meta:
        model = PostInfo
        fields = ('title', 'description', 'author', 'category')

class ProfileLookupSerializer(serializers.ModelSerializer):
    postUser = PostInfoListSerializer(many=True,read_only = True)
    commentUser = CommentSerializer(many=True,read_only= True)
    class Meta:
        model = Auth
        fields = ('nickname','uid','password','postUser','commentUser')