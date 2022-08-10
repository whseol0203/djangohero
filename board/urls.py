from django.urls import path

from .views import userRegisterAPI, userLoginAPI

# 220810
from .views import boardAPI

urlpatterns = [
    path('register/', userRegisterAPI.as_view()),
    path('login/',userLoginAPI.as_view()),

    # 220810
    path('board/', boardAPI.as_view()),
]
