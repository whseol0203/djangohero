from django.contrib import admin
from .models import Auth

# 220810
from .models import Info

# Register your models here.
admin.site.register(Auth)

# 220810
admin.site.register(Info)