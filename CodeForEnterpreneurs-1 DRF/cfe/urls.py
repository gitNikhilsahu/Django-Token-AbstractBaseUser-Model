from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cfe import views


router = DefaultRouter()
router.register('cfe-viewset', views.cfe_view_set, basename='cfe-viewset')

urlpatterns = [
    path('', include(router.urls))
]
