
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:board_id>/', views.detail),
    path('post', views.post)
]