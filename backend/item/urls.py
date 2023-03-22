from django.urls import path

from item.views import ListCreateItemView, RetrieveUpdateDeleteItemView

urlpatterns = [
    path("", ListCreateItemView.as_view()),
    path("<int:id>/", RetrieveUpdateDeleteItemView.as_view()),
]
