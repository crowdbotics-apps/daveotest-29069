from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    ReviewViewSet,
    ItemViewSet,
    CategoryViewSet,
    CountryViewSet,
    ItemVariantViewSet,
)

router = DefaultRouter()
router.register("review", ReviewViewSet)
router.register("item", ItemViewSet)
router.register("itemvariant", ItemVariantViewSet)
router.register("category", CategoryViewSet)
router.register("country", CountryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
