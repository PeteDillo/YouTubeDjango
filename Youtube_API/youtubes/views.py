from django.http.response import Http404
from django.shortcuts import render
from .models import Comment
from .models import Reply
from .serializers import CommentsSerializer
from .serializers import ReplySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class CommentList(APIView):

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetail(APIView):

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        comments = self.get_object(pk)
        serializer = CommentsSerializer(comments)
        return Response(serializer.data)

    def put(self, request, pk):
        comments = self.get_object(pk)
        serializer = CommentsSerializer(comments, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comments = self.get_object(pk)
        comments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReplyList(APIView):

    def get(self, request):
        replies = Reply.objects.all()
        serializer = ReplySerializer(replies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReplyDetail(APIView):

    def get_object(self, pk):
        try:
            return Reply.objects.get(pk=pk)
        except Reply.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        replies = self.get_object(pk)
        serializer = ReplySerializer(replies)
        return Response(serializer.data)

    def put(self, request, pk):
        replies = self.get_object(pk)
        serializer = ReplySerializer(replies, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        replies = self.get_object(pk)
        replies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)