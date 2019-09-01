from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CarListView.as_view(), name='root'),
]
