
from http.client import HTTPResponse
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from django.http import HttpResponse


from .models import Auth, Comment
from .serializers import RegisterSerializer, LoginSerializer, CommentSerializer, LikeUserSerializer, ProfileLookupSerializer

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
    @swagger_auto_schema(
        operation_summary="유저 회원가입",
        operation_description="""
            ### 회원가입 합니다.
            ---
            ### 파라미터 
            1. nickname : 가입할 유저의 닉네임
            2. uid : 가입할 유저의 id (고유 id 아님), 중복되는 id 가 있을 경우 오류 발생
            3. password : 가입할 유저의 비밀번호
            ---
            parameters 내의 Example Value, Model 전환 버튼을 이용하면 더 편하게 이용할 수 있습니다.
            try it out 시 데이터베이스에 실제로 데이터가 쌓이니 왠만하면 사용하지 말 것.
            
        """,
        responses={
            200 :'''
                {
                  "nickname": "swagger",
                  "uid": "sw",
                  "password": "swagger"
                }
                다음과 같은 형태가 반환되며, 회원가입 성공
            ''',
            401 : '중복되는 아이디가 존재함',
            404 : 'post 형식이 맞지 않음'
        },
        request_body=RegisterSerializer
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
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
    @swagger_auto_schema(
        operation_summary="로그인",
        operation_description="""
            ### 로그인합니다.
            ---
            ### 파라미터 
            1. uid : 로그인 할 유저의 아이디 (고유 id 아님)
            2. password : 로그인 할 유저의 비밀번호.
            ---
            parameters 내의 Example Value, Model 전환 버튼을 이용하면 더 편하게 이용할 수 있습니다.
            try it out 사용 가능
        """,
        responses={
            200 :'''
                {
                  "uid": "sw",
                  "password": "swagger"
                }
                다음과 같은 형태가 반환되며, 로그인 성공
            ''',
            401 : '존재하지 않는 id',
            406 : '비밀번호 불일치',
            404 : 'post 형식이 맞지 않음'
        },
        request_body=LoginSerializer
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            if Auth.objects.filter(uid=serializer.validated_data['uid']).exists():
                inputId = serializer.validated_data['uid']
                dbObj = get_object_or_404(Auth,uid=inputId)
                inputPassword = serializer.validated_data.get('password')
                if dbObj.password == inputPassword:
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.data, status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
        else: 
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
            ### 파라미터 
            1. postUser : 게시한 유저의 고유 id. 안 적어도 상관없다 적혀 있지만 반드시 적어야 함. 중요 
            2. title : 게시글 제목
            3. author : 게시글 작성자 닉네임
            4. category : 게시글 카테고리
            5. views : 게시글 조회수. 적지 않아도 상관없으며, 적어야 하면 0으로 적을 것.
            ---
            parameters 내의 Example Value, Model 전환 버튼을 이용하면 더 편하게 이용할 수 있습니다.
            try it out 시 데이터베이스에 실제로 데이터가 쌓이니 왠만하면 사용하지 말 것.
        """,
        responses={
            200 : 
            '''
            {
                "postUser": 1,
                "title": "string",
                "author": "string",
                "time": "16:04:10.104645",
                "category": "string",
                "views": 0
            }
            다음과 같은 반환 형태를 가지며 (예시), 게시글 업로드 성공 
            ''',
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
    @swagger_auto_schema(
        operation_summary="특정 게시글 조회",
        operation_description="""
            ### 특정 게시글을 조회합니다.
            ---
            ### /board/{게시글 id}/ 형태로 호출합니다.
            
            try it out을 사용하여 시험 가능.
        """,
        responses={
            200 : '조회 결과가 같이 도착하며, 게시글 조회 성공'
        },
    )
    def get(self, request, id):
        board = get_object_or_404(PostInfo, id=id)
        serializer = PostInfoDetailSerilizer(board)
        return Response(serializer.data, status=status.HTTP_200_OK)


class commentAPI(APIView):
     # 댓글 전체 조회
    @swagger_auto_schema(
        operation_summary="댓글 전체 조회",
        operation_description="""
            ### 전체 댓글을 조회합니다.
            ---
            파라미터 없음.
            ---
            try it out을 사용하여 시험 가능.
        """,
        responses={
            200 : '전체 사용자의 댓글이 전부 조회되며, 조회 성공'
        }
    )
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 댓글 업로드
    @swagger_auto_schema(
        operation_summary="댓글 업로드",
        operation_description="""
            ### 댓글을 업로드합니다.
            ---
            ### 파라미터 
            1. commentedPost : 댓글이 위치한 글의 고유 id. 안 적어도 상관없다 적혀 있지만 반드시 적어야 함. 중요 
            2. commentUser : 게시한 유저의 고유 id. 안 적어도 상관없다 적혀 있지만 반드시 적어야 함. 중요 
            3. nickname : 게시한 유저의 닉네임.
            4. contents : 게시한 댓글의 내용.
            ---
            parameters 내의 Example Value, Model 전환 버튼을 이용하면 더 편하게 이용할 수 있습니다.
            try it out 시 데이터베이스에 실제로 데이터가 쌓이니 왠만하면 사용하지 말 것.
            
        """,
        responses={
            200 :'''
                {
                    "commentedPost": 1,
                    "commentUser": 1,
                    "nickname": "string",
                    "time": "15:58:42.318989",
                    "contents": "string"
                }
                다음과 같은 형태가 반환되며, 댓글 업로드 성공
            ''',
            404 : 'post 형식이 맞지 않음'
        },
        request_body=CommentSerializer
    )
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class profileLookupAPI(APIView):
     # 프로파일 조회
    @swagger_auto_schema(
        operation_summary="유저 프로필 조회",
        operation_description="""
            ### 특정 유저의 프로필을 조회합니다.
            ---
            ### /profile/{유저 id (고유 id 아님)}/ 형태로 호출합니다.
            
            try it out을 사용하여 시험 가능.
        """,
        responses={
            200 : '조회 결과가 같이 도착하며, 프로필 조회 성공'
        },
    )
    def get(self, request, uid):
        user = get_object_or_404(Auth, uid=uid)
        serializer = ProfileLookupSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 좋아요 수동 추가용도 

class likeAddAPI(APIView):
    @swagger_auto_schema(
        operation_summary="좋아요 추가",
        operation_description="""
            ### 좋아요를 추가합니다.
            ---
            ### 파라미터 
            1. likeUser : 좋아요를 한 유저의 고유 id. 안 적어도 상관없다 적혀 있지만 반드시 적어야 함. 중요 
            2. targetPost : 좋아요를 한 게시글의 고유 id. 안 적어도 상관없다 적혀 있지만 반드시 적어야 함. 중요 
            ---
            parameters 내의 Example Value, Model 전환 버튼을 이용하면 더 편하게 이용할 수 있습니다.
            try it out 시 데이터베이스에 실제로 데이터가 쌓이니 왠만하면 사용하지 말 것.

        """,
        responses={
            200 :'''
                {
                    "likeUser": 1,
                    "targetPost": 1
                }
                다음과 같은 형태가 반환되며, 좋아요 성공
            ''',
            404 : 'post 형식이 맞지 않음'
        },
        request_body=LikeUserSerializer
    )
    def post(self, request):
        serializer = LikeUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
