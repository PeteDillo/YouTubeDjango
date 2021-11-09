from django.http.response import Http404
from django.shortcuts import render
from rest_framework.serializers import Serializer
from .models import Song
from .serializers import SongSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
