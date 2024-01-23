from django.urls import path
from . import views

urlpatterns = [
    path('', views.producers, name='producers'),
    path('add_producer', views.add_producer, name='add_producer'),
    path('edit_producer/<int:producer_id>/', views.edit_producer, name='edit_producer'),
    path('delete/<int:product_id>/', views.delete_producer, name='delete_producer'),
]
