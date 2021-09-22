from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ProfileViewSet, ContactInfoViewSet

router = DefaultRouter()
router.register("contactinfo", ContactInfoViewSet)
router.register("profile", ProfileViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
