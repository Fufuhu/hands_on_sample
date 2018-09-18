from guestbook_plus.models.comments import Comment
from guestbook_plus.models.users import Commentator
from guestbook_api.serializers.thread_serializers import ThreadSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CommentThreadApiView(APIView):

    def get_leafs(self, root):
        """
        rootに指定したコメントをrootとしてそこにぶら下がるすべての
        コメントを配列として取得します。
        """
        leafs = Comment.objects.filter(parent=root)
        self.tree = self.tree + list(leafs)

        if leafs.count() == 0:
            return self.tree
        else:
            for leaf in leafs:
                self.get_leafs(root=leaf)

    def get(self, request, comment_id, format=None):

        root_comment = Comment.objects.get(comment_id=comment_id)

        while root_comment.parent is not None:
            root_comment = root_comment.parent
        self.tree = [ root_comment ]
        self.get_leafs(root=root_comment)

        thread = {
            'title': root_comment.title,
            'comments': self.tree,
        }

        serializer =  ThreadSerializer(thread)
        return Response(serializer.data)

        