from rest_framework import serializers
from guestbook_plus.models.users import Commentator


class CommentatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentator
        fields = '__all__'