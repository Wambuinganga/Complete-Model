from django.contrib import admin
from django.urls import path,include
from . import views
from .views import status
from rest_framework import routers

router = routers.DefaultRouter()
urlpatterns = [
  path('api/', include(router.urls)),
  path("status/", status, name="status"),
  ]
