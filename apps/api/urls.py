from django.urls import re_path, include
from rest_framework import routers
from apps.api import views
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls)),
]