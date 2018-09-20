from django.views.generic import View
from django.shortcuts import render, redirect
from ..models.comments import Comment
from ..models.users import Commentator
from django.core.exceptions import ObjectDoesNotExist


class CommentThreadView(View):


    def get(self, request, comment_id):
        root_comment = Comment.objects.get(comment_id=comment_id)
        response_params = {
            'title': root_comment.title,
            'comments': root_comment.get_thread(),
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