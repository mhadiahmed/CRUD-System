from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^books/$', views.book_list, name='book_list'),
    url(r'^books/create$', views.book_create, name='book_create'),
    url(r'^books/(?P<id>\d+)/update$', views.book_update, name='book_update'),
    url(r'^books/(?P<id>\d+)/delete$', views.book_delete, name='book_delete'),
]