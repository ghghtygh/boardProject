
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:board_id>/', views.detail),
    path('modify/<int:board_id>/', views.modify),
    path('delete/<int:board_id>/', views.delete),
    path('post', views.post)
]