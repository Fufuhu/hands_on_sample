from django.conf.urls import url
from guestbook_plus.views.base_view import BaseView
from .views.comment_list_view import CommentListView
from .views.comment_thread_view import CommentThreadView

app_name = 'guestbook_plus'

urlpatterns = [
    url(r'^$', BaseView.as_view(), name='base'),
    url(r'^comments/$', CommentListView.as_view(), name='comment_list'),
    url(r'^comments/(.+)/$', CommentThreadView.as_view(), name='comment_thread'),
]