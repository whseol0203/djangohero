from dataclasses import field
from rest_framework import serializers
from .models import Auth

# 220810
from .models import Info

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auth
        fields = ('userId',"password","email")

# 220810
class InfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ('title', 'description', 'category')

# 220810
class InfoDetailSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ('title', 'description', 'author', 'category')