from django.urls import path
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('secret/', views.secret, name='secret'),
    path('accounts/', include("django.contrib.auth.urls")),
]