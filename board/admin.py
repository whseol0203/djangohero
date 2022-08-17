from django.contrib import admin
from .models import Auth, PostInfo

# 220817 admin에 LikeInfo, Comment 추가
from .models import LikeInfo, Comment

# Register your models here.
admin.site.register(Auth)
admin.site.register(PostInfo)

# 220817
admin.site.register(LikeInfo)
admin.site.register(Comment)