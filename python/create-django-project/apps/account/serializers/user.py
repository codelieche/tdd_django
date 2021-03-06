# -*- coding:utf-8 -*-
from rest_framework import serializers

from account.models import User, SafeLog


class UserLoginSerializer(serializers.Serializer):
    """用户登录 Serializer"""
    username = serializers.CharField(max_length=40, required=True)
    password = serializers.CharField(max_length=40, required=True)


class UserSimpleInfoSerializer(serializers.ModelSerializer):
    """
    用户基本信息Model Serializer
    """

    class Meta:
        model = User
        fields = ('id', 'username')


class UserAllListSerializer(serializers.ModelSerializer):
    """
    列出所有用户的信息Model Serializer
    """

    class Meta:
        model = User
        fields = ('id', 'username', 'nick_name', 'mobile', 'dingding', 'wechart',
                  'is_superuser', 'is_active', 'last_login', 'is_deleted')


class UserDetailSerializer(serializers.ModelSerializer):
    """
    用户详情/编辑序列化Model
    """

    class Meta:
        model = User
        fields = ('id', 'username', 'nick_name', 'is_active', 'mobile',
                  'dingding', 'wechart',
                  'is_superuser', 'last_login', 'is_deleted')
        read_only_fields = ('id', 'username', 'last_login')


class SafeLogModelSerializer(serializers.ModelSerializer):
    """
    Safe Log Model Serializer
    """
    user = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())
    category_verbose = serializers.CharField(read_only=True, required=False, source="get_category_display")

    class Meta:
        model = SafeLog
        fields = ("id", "user", "category", "content", "category_verbose", "ip", "devices", "is_ok", "time_added")
