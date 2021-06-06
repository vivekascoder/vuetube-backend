from django.urls import path
from app import views

urlpatterns = [
  path('category', views.CategoryList.as_view(), name='category-list'),
  path('category/<int:pk>', views.CategoryDetail.as_view(), name='category-detail'),
  path(views.CategoryLinks.endpoint, views.CategoryLinks.as_view(), name='category-link-list'),
  path('link', views.LinkList.as_view(), name='link-list'),
  path('link/<int:pk>', views.LinkDetail.as_view(), name='link-detail'),
]