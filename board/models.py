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
    # 게시한 사용자 추적
    postUser = models.ForeignKey(Auth, null=True, on_delete=models.CASCADE, db_column="postUser", related_name="post")
    title = models.CharField(max_length=50)
    contents = models.CharField(max_length=300)
    author = models.CharField(max_length=50)
    time = models.TimeField(auto_now=False, auto_now_add=True)
    # media = 일단 보류
    category = models.CharField(max_length=30)
    views = 0


'''
수정일 : 220817
좋아요 표시를 위한 모델
'''
class LikeInfo(models.Model):
    likeUser = models.ForeignKey(Auth, null=True, on_delete=models.CASCADE, db_column="likeUser", related_name="userlike")
    targetPost = models.ForeignKey(PostInfo, null=True, on_delete=models.CASCADE, db_column="targetPost", related_name="targetPost")


'''
수정일 : 220811
댓글 모델

nickname : 유저 이름
time : 작성 시간
contents : 작성 내용
'''
class Comment(models.Model):
    # 댓글 단 유저 추적
    commentUser = models.ForeignKey(Auth, null=True,on_delete=models.CASCADE,db_column="commentUser",related_name="comment")
    nickname = models.CharField(max_length=50)
    time = models.TimeField(auto_now=False, auto_now_add=True)
    contents = models.CharField(max_length=100)

