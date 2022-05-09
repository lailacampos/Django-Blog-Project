# Mapping urls to view functions (request handlers)

from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register')
]
