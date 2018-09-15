from django.views.generic import View
from django.shortcuts import render, redirect
from ..models.comments import Comment
from ..models.users import Commentator
from django.core.exceptions import ObjectDoesNotExist


class CommentThreadView(View):

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

    def get(self, request, comment_id):

        root_comment = Comment.objects.get(comment_id=comment_id)
        while root_comment.parent is not None:
            root_comment = root_comment.parent
        self.tree = [root_comment]
        self.get_leafs(root=root_comment)


        response_params = {
            'title': root_comment.title,
            'comments': self.tree,
        }

        return render(request, 'comment_thread.html', response_params)

    def post(self, request, comment_id):
        parent = Comment.objects.get(comment_id=comment_id)

        commentator = None
        try:
            commentator = Commentator.objects.get(name=request.POST.get('name'))
        except ObjectDoesNotExist as err:
            commentator = Commentator(
                name=request.POST.get('name')
            )
            commentator.save()


        comment = Comment(
            title=request.POST.get('title'),
            comment=request.POST.get('comment'),
            commentator=commentator,
            parent=parent
        )
        comment.save()

        return self.get(request, comment_id=comment_id)