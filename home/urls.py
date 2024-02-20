from django.urls import path
from . import views
from django.conf.urls import handler404

urlpatterns = [
    path('', views.index, name='home'),
    path('privacy/', views.privacy, name='privacy_policy'),
]

handler404 = "home.views.view404"