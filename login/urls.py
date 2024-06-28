from django.urls import path
from login.views import *

urlpatterns = [
    path('', loginFormView.as_view(), name='login'),
    path('logout', logoutRedirect.as_view(), name='logout')
]
