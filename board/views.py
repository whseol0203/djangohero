

from email import message
from enum import unique
from msilib.schema import ServiceInstall
from unicodedata import name
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view



from .models import Auth
from .serializers import AuthSerializer
from board import serializers

# 220810
from .models import Info
from .serializers import InfoSerializer

# Create your views here.

# user resgister API
class userRegisterAPI(APIView):

    def post(self, request):
        serializer = AuthSerializer(data=request.data)
        if serializer.is_valid():
            if Auth.objects.filter(userId=serializer.validated_data['userId']).exists():
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
            
            inputId = serializer.validated_data['userId']
            inputPassword = serializer.validated_data.get('password')
            print("hello")

            dbObj = get_object_or_404(Auth,userId=inputId)

            if dbObj.password == inputPassword:
                print("correct id")
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

# 220810
# 게시글 전체 조회, 업로드
class boardsAPI(APIView):

    # 게시글 전체 조회
    def get(self, request):
        boards = Info.objects.all()
        serializer = InfoSerializer(boards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 게시글 업로드
    def post(self, request):
        serializer = InfoSerializer(dta=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)