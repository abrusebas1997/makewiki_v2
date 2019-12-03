from django.urls import path
from . import views


urlpatterns = [
    path('maps/', views.default_map, name='default'),
]
