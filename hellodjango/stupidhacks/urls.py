from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.stupidhacks, name='stupidhacks'),
    re_path(r'^submit', views.submit)
]