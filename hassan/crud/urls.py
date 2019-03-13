from django.urls import path
from crud import views

urlpatterns = [
    path('crud/', views.crud_list),
    path('crud/<int:pk>/', views.crud_detail),
]