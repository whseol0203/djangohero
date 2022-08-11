from django.contrib import admin
from .models import Auth

# 220810
from .models import PostInfo

# Register your models here.
admin.site.register(Auth)

# 220810
admin.site.register(PostInfo)