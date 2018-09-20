from django.db import models
import uuid

from .users import Commentator

class Comment(models.Model):
    comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=100, blank=False)
    comment = models.TextField(blank=False)
    commentator = models.ForeignKey(to=Commentator, on_delete=models.CASCADE, blank=True)
    parent = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='oyako', null=True)
    append_at = models.DateTimeField(auto_now_add=True)

    def get_thread(self):
        """
        特定のcommentからcommentの所属するスレッド全体を取得する
        """

        comment = self
        while comment.parent is not None:
            comment = comment.parent
        
        self.tree = [comment]
        self.__get_leafs(root=comment)

        return self.tree
        
    
    def __get_leafs(self, root):
        leafs = Comment.objects.filter(parent=root)

        self.tree = self.tree + list(leafs)

        if leafs.count() == 0:
            return self.tree
        else:
            for leaf in leafs:
                self.__get_leafs(root=leaf)