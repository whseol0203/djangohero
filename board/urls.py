import profile
from django.urls import path

from .views import userRegisterAPI, userLoginAPI, commentAPI, profileLookupAPI

# 220810
from .views import boardsAPI, boardAPI

urlpatterns = [
    path('register/', userRegisterAPI.as_view()),
    path('login/',userLoginAPI.as_view()),

    # 220810
    path('board/', boardsAPI.as_view()),
    path('board/<int:id>/', boardAPI.as_view()),

    path('comment/', commentAPI.as_view()),
    path('profile/<str:uid>/',profileLookupAPI.as_view())
]
