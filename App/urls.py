from django.contrib import admin
from django.urls import path, include 
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('article',views.ArticleViewSetModel, basename='article')

urlpatterns = [
    
    path('viewset/', include(router.urls)),
    path('viewset/<str:pk>/', include(router.urls)),
    
    path('',  views.index, name='index'),
    #path('article', views.article_list, name='article'),
    path('article', views.ArticleAPIView.as_view(), name='article'),
    
    #path('details/<str:pk>/', views.article_details, name='article_details'),
    path('details/<str:pk>/', views.Details.as_view(), name='article_details'),
    path('generic/',  views.Generic.as_view(), name='generic'), 
    path('generic/<str:pk>',  views.GenericDetails.as_view(), name='generic'),
       
]