from django.db import models

# Create your models here.
# class Auth(models.Model):
#     userId = models.CharField(max_length=50)
#     password = models.CharField(max_length=100)
#     email = models.CharField(max_length=50, unique=True, blank=True)

# 220810
# class Info(models.Model):
#     title = models.CharField(max_length=50)
#     description = models.CharField(max_length=50)
#     author = models.CharField(max_length=50)
#     category = models.CharField(max_length=50)

# 220811
# Authentication 모델 수정 -> 닉네임 추가
class Auth(models.Model):
    userName = models.CharField(max_length=50)
    userId = models.CharField(max_length=50)
    password = models.CharField(max_length=100)


# Info 모델 수정 -> 게시글 항목
class Info(models.Model):
    title = models.CharField(max_length=50)
    contents = models.CharField(max_length=300)
    author = models.CharField(max_length=50)
    time = models.TimeField(auto_now=False, auto_now_add=True)
    # media = 일단 보류
    category = models.CharField(max_length=30)

# 댓글 모델
class Comment(models.Model):
    userName = models.CharField(max_length=50)
    time = models.TimeField(auto_now=False, auto_now_add=True)
    contents = models.CharField(max_length=100)