from django.db import models

'''
수정일 : 220811
Authentication 모델 수정 -> 닉네임 추가

nickname : 유저 닉네임
uid : 유저 ID
Password : 유저 비밀번호
'''
class Auth(models.Model):
    nickname = models.CharField(max_length=50)
    uid = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)



'''
수정일 : 220811
Info 모델 수정 -> 게시글 항목
Info -> PostInfo 로 바꾸는 건 어떰

title : 제목
contents : 내용
author : 작성한 사람
time : 작성한 시간
category : 게시글 카테고리
likeUserNicknameList : 좋아요 누른 사람들의 닉네임 리스트
commentUserIdList : 댓글 단 사람들의 id 리스트
views : 본 사람의 수 
'''
class PostInfo(models.Model):
    postUser = models.ForeignKey(Auth, null=True, on_delete=models.CASCADE, db_column="postUser", related_name="postUser")
    title = models.CharField(max_length=50)
    contents = models.CharField(max_length=300)
    author = models.CharField(max_length=50)
    time = models.TimeField(auto_now=False, auto_now_add=True)
    # media = 일단 보류
    category = models.CharField(max_length=30)

    likeUserNicknameList = []
    commentUserIdList = []
    views = 0



'''
수정일 : 220811
댓글 모델

nickname : 유저 이름
time : 작성 시간
contents : 작성 내용
'''
class Comment(models.Model):
    commentUser = models.ForeignKey(Auth, null=True,on_delete=models.CASCADE,db_column="commentUser",related_name="commentUser")
    nickname = models.CharField(max_length=50)
    time = models.TimeField(auto_now=False, auto_now_add=True)
    contents = models.CharField(max_length=100)


'''
수정일 : 220811
프로필 모델

nickname : 유저 이름
uid : 유저 아이디
postIdList : 게시한 게시글 id 리스트
commentIdList : 작성한 댓글 id 리스트
likePostIdList : 좋아요를 누른 게시글 아이디
'''
class Profile(models.Model):
    nickname = models.CharField(max_length=50)
    uid = models.CharField(max_length=50)
    postIdList = []
    commentIdList = []
    likePostIdList = []