from django.urls import path, include
from rest_framework.routers import DefaultRouter

from article import views


router = DefaultRouter()
router.register('article-viewset', views.article_view_set, basename='article-viewset')

urlpatterns = [
    path('', include(router.urls))
]
