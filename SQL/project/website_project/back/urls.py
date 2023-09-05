from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("index",views.index),
    path("blog",views.blog),
    path("blog/<int:id>",views.blog_details),
]