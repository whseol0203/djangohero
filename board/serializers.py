from dataclasses import field
from rest_framework import serializers
from .models import Auth, Comment

# 220817
# CommentSerializer time field 추가
from .models import PostInfo

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auth
        fields = ('nickname','uid','password')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('commentUser','nickname','time','contents')



# 220817 List field 추가, Detail field 추가, comments list 에서 detail로 이동
# 게시글 리스트
class PostInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostInfo
        fields = ('postUser', 'title', 'author', 'time', 'category', 'views')

# 게시글 상세 조회
class PostInfoDetailSerilizer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = PostInfo
        fields = ('postUser', 'title', 'contents', 'author', 'category', 'views', 'comments')

class ProfileLookupSerializer(serializers.ModelSerializer):
    post = PostInfoListSerializer(many=True,read_only = True)
    comments = CommentSerializer(many=True,read_only= True)
    class Meta:
        model = Auth
        fields = ('nickname','uid','password','post','comments')