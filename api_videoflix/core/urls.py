from django.urls import include, path
from rest_framework import routers
from .views import VideoViewSet


router = routers.DefaultRouter()
router.register(r"videos", VideoViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
