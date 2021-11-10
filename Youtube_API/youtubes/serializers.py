from rest_framework import serializers
from .models import Comment
from .models import Reply


class CommentsSerializer (serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'video_id', 'comment', 'like', 'dislike']

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['id', 'comment', 'reply']