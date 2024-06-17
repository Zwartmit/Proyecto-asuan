from django.urls import path
from app.views import *

urlpatterns = [
    path('uno/', vista1),
    path('dos/', vista2)
]
