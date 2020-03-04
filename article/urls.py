from django.urls import path
from article import views

urlpatterns = [
    path('', views.article_list_view.as_view()),
    path('<slug:slug>/', views.article_detail_view.as_view()),
    path('retrive/<int:id>/', views.article_retrive_view.as_view()),
    path('create/', views.article_create_view.as_view()),
    path('article_rud/<int:id>/', views.article_retrive_update_destroy_view.as_view()),
    # path('update/<int:id>/', views.article_update_view.as_view()),
    # path('destroy/<int:id>/', views.article_destroy_view.as_view()),
]
