from django.urls import path

from .views import userRegisterAPI, userLoginAPI

urlpatterns = [
    path('register/', userRegisterAPI.as_view()),
    path('login/',userLoginAPI.as_view())
]
