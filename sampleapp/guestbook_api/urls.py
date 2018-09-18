from django.conf.urls import url
from .views.comment_list_api import CommentListApiView
from .views.comment_thread_api import CommentThreadApiView

app_name = 'guestbook_api'

urlpatterns = [
    url(r'^comments/$', CommentListApiView.as_view(), name='comment_list_api'),
    url(r'^comments/(.+)/$', CommentThreadApiView.as_view(), name='comment_thread_api'),
]