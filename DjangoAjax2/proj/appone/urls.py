from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('selectlocation', views.selectLocation),
    path('selectasset', views.selectAssets),
]
