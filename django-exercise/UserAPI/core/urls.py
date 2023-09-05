from django.urls import path
from core.api.views import UserClassBaseView

urlpatterns = [
    path("", UserClassBaseView.as_view()),
    path("<pk>", UserClassBaseView.as_view()),
]
