
from http.client import HTTPResponse
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from django.http import HttpResponse


from .models import Auth, Comment
from .serializers import AuthSerializer, CommentSerializer, ProfileLookupSerializer

# 220810
from .models import PostInfo
from .serializers import PostInfoListSerializer
from .serializers import PostInfoDetailSerilizer

# Create your views here.

# user resgister API
class userRegisterAPI(APIView):

    def post(self, request):
        serializer = AuthSerializer(data=request.data)
        if serializer.is_valid():
            if Auth.objects.filter(uid=serializer.validated_data['uid']).exists():
                print("exceiption")
                #raise IdInformationDuplicateException
                return Response(serializer.errors,status=status.HTTP_401_UNAUTHORIZED)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        

class userLoginAPI(APIView):

    def post(self, request):
        serializer = AuthSerializer(data=request.data)
        
        if serializer.is_valid():
            
            inputId = serializer.validated_data['uid']
            inputPassword = serializer.validated_data.get('password')
            print("hello")

            dbObj = get_object_or_404(Auth,uid=inputId)

            if dbObj.password == inputPassword:
                print("correct id")
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

# 220810
# 게시글 전체 조회, 업로드, 특정 게시글 열람
class boardsAPI(APIView):

    # 게시글 전체 조회
    def get(self, request):
        boards = PostInfo.objects.all()
        serializer = PostInfoListSerializer(boards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 게시글 업로드
    def post(self, request):
        serializer = PostInfoListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

# 특정 게시글 열람
class boardAPI(APIView):

    # 게시글 조회
    def get(self, request, id):
        board = get_object_or_404(PostInfo, id=id)
        serializer = PostInfoDetailSerilizer(board)
        return Response(serializer.data, status=status.HTTP_200_OK)


class commentAPI(APIView):
     # 댓글 전체 조회
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 댓글 업로드
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class profileLookupAPI(APIView):
     # 프로파일 조회
    def get(self, request, uid):
        user = get_object_or_404(Auth, uid=uid)
        serializer = ProfileLookupSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

