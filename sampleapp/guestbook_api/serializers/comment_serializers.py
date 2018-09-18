from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from guestbook_plus.models.comments import Comment
from guestbook_plus.models.users import Commentator
from guestbook_api.serializers.user_serializers import CommentatorSerializer


class CommentSerializer(serializers.ModelSerializer):
    commentator = SerializerMethodField()
    class Meta:
        model = Comment
        fields = [
            'comment_id',
            'title',
            'comment',
            'commentator',
            'parent',
            'append_at',
        ]

    def get_commentator(self, obj):
        return CommentatorSerializer(obj.commentator).data