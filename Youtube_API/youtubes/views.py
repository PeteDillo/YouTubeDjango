from django.http.response import Http404
from django.shortcuts import render
from rest_framework.serializers import Serializer
from .models import Video
from .serializers import VideoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class VideoList(APIView):

    def get(self, request):
        video = Video.objects.all()
        serializer = VideoSerializer(video, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)