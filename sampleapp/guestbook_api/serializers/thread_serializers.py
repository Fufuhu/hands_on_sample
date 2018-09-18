from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from django.db import models
from guestbook_plus.models.comments import Comment
from guestbook_plus.models.users import Commentator
from guestbook_api.serializers.user_serializers import CommentatorSerializer
from .comment_serializers import CommentSerializer

class ThreadSerializer(serializers.Serializer):
    title = models.CharField(max_length=100)
    comments = CommentSerializer(many=True)
