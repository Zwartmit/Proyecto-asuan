from django.contrib import admin
from django.urls import path, include
from inicio.views import indexView
from login.views import *
from app.views import *
from dashboard.views import *

urlpatterns = [
    path('', indexView.as_view(), name='index'),
    path('dashboard', dashView.as_view(), name='dashboard'),
    path('login', include('login.urls')),
    path('admin/', admin.site.urls),
    path('app/', include('app.urls'))
]
