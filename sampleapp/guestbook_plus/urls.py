from django.conf.urls import url
from guestbook_plus.views.base_view import BaseView

app_name = 'guestbook_kai'

urlpatterns = [
    url(r'^$', BaseView.as_view(), name='base'),
]