from django.db import models
import uuid

from .users import Commentator

class Comment(models.Model):
    comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    comment = models.TextField(blank=False)
    commentator = models.ForeignKey(to=Commentator, on_delete=models.CASCADE)