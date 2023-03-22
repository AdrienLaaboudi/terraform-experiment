from django.urls import path

from order.views import ListCreateOrderView, RetrieveUpdateDeleteOrderView

urlpatterns = [
    path("", ListCreateOrderView.as_view()),
    path("<int:id>/", RetrieveUpdateDeleteOrderView.as_view()),
]
