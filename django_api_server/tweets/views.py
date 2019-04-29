from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Tweet
from .serializer import TweetsSerializer


class TweetsViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetsSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Tweet.objects.exclude(user=self.request.user).order_by("-created_at")
        else:
            return Tweet.objects.order_by("-created_at")

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if not request.user == instance.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)
