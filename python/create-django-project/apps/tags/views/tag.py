# -*- coding:utf-8 -*-
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.permissions import IsAuthenticated

from tags.models import Tag
from tags.serializers.tags import TagModelSerializer


class TagCreateApiView(generics.CreateAPIView):
    """
    创建标签
    """
    queryset = Tag.objects.all()
    serializer_class = TagModelSerializer
    permission_classes = (IsAuthenticated,)


class TagListApiView(generics.ListAPIView):
    """
    标签列表api
    """
    queryset = Tag.objects.filter(is_deleted=False)
    serializer_class = TagModelSerializer
    permission_classes = (IsAuthenticated,)


class TagDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    """
    标签详情api
    """
    queryset = Tag.objects.all()
    serializer_class = TagModelSerializer
    permission_classes = (IsAuthenticated, )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response(status=HTTP_204_NO_CONTENT)
