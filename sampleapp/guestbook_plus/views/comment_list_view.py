from django.views.generic import View
from django.shortcuts import render, redirect
from ..models.comments import Comment
from ..models.users import Commentator
from django.core.exceptions import ObjectDoesNotExist

class CommentListView(View):
    def get(self, request, comment_id=None):
        comments = Comment.objects.filter(parent=None)
        response_params = {
            'comments': comments,
        }
        return render(request, 'comment_list.html', response_params)

    def post(self, request, comment_id=None):

        name = request.POST.get('name')

        commentator = None
        try:
            commentator = Commentator.objects.get(name=name)
        except ObjectDoesNotExist as err:
            print(err)

        if commentator is None:
            commentator = Commentator(name=name)
            commentator.save()

        title = request.POST.get('title')
        comment = request.POST.get('comment')

        if comment_id is None:
            # ルートコメント(新規スレッド作成の場合) 
            comment = Comment(
                title=title,
                comment=comment,
                commentator=commentator
            )
        else:
            # スレッドへの投稿の場合
            pass
        
        comment.save()

        print(commentator)

        comments = Comment.objects.filter(parent=None)

        response_params = {
            'comments': comments,
        }
        return redirect(to='guestbook/comments/')
        # return render(request, 'comment_list.html', response_params)