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
        fields = ('post_id','nickname','contents')



# 220810
class PostInfoListSerializer(serializers.ModelSerializer):
    postInfo = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = PostInfo
        fields = ('title', 'category', 'postInfo')

# 220810
class PostInfoDetailSerilizer(serializers.ModelSerializer):
    class Meta:
        model = PostInfo
        fields = ('title', 'description', 'author', 'category')