from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.poll_list),
    path('about/', views.about),
]
