from guestbook_plus.models.comments import Comment
from guestbook_plus.models.users import Commentator
from guestbook_api.serializers.comment_serializers import CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CommentListApiView(APIView):

    def get(self, request, format=None):
        comments = Comment.objects.filter(parent=None)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)