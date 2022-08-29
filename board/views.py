
from http.client import HTTPResponse
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from django.http import HttpResponse


from .models import Auth, Comment
from .serializers import AuthSerializer, CommentSerializer, LikeUserSerializer, ProfileLookupSerializer

# 220810
from .models import PostInfo
from .serializers import PostInfoListSerializer
from .serializers import PostInfoDetailSerilizer

# swagger decorate
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

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

# 220817
# 게시글 전체 시간 역순 조회
class boardsAPI(APIView):
    '''
    Board 조회 및 업로드
    ---
    test code
    '''

    # 게시글 전체 조회
    @swagger_auto_schema(
        operation_summary="게시글 전체 조회",
        operation_description="""
            ### 게시글의 전체 정보를 불러옵니다.
            ---
            파라미터 없음.
        """,
        responses={
            200 : '게시글 불러오기 성공'
        }
    )
    def get(self, request):
        boards = PostInfo.objects.order_by('time').reverse()
        serializer = PostInfoListSerializer(boards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # 게시글 업로드
    @swagger_auto_schema(
        operation_summary="게시글 업로드",
        operation_description="""
            ### 게시글을 업로드합니다.
            ---
            #### 파라미터 
            1. postUser : 게시한 유저의 고유 id. 안 적어도 상관없다 적혀 있지만 반드시 적어야 함. 중요 
            2. title : 게시글 제목
            3. author : 게시글 작성자 닉네임
            4. category : 게시글 카테고리
            5. views : 게시글 조회수. 적지 않아도 상관없으며, 적어야 하면 0으로 적을 것.
            ---
            parameters 내의 Example Value, Model 전환 버튼을 이용하면 더 편하게 이용할 수 있습니다.
        """,
        responses={
            200 : '게시글 포스트 성공',
            404 : 'post 형식이 맞지 않음'
        },
        request_body=PostInfoListSerializer
    )
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

# 테스트 코드
# 좋아요 수동 추가용도 
class likeAddAPI(APIView):
    def post(self, request):
        serializer = LikeUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
