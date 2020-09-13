from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('wines/', views.WineList.as_view(), name='wine_list'),
    path('wines/<int:pk>', views.WineDetail.as_view(), name='wine_detail'),
]
