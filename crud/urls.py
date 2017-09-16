from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^books/$', views.book_list, name='book_list'),
]