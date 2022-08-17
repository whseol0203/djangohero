from django.contrib import admin
from .models import Auth

# 220817 추가 모델들 = Comment, Profile
from .models import Comment, Profile

# 220810
from .models import PostInfo

# Register your models here.
admin.site.register(Auth)

# 220810
admin.site.register(PostInfo)

# 220817 추가 모델들 admin 추가
admin.site.register(Comment)
admin.site.register(Profile)