from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CategoryCreateAPIView, create_blog, update_blog, delete_blog, BlogViewSet

router = DefaultRouter()
router.register('blogs', BlogViewSet)

urlpatterns = [
    path('category-create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('blog-create/', create_blog, name='blog-create'),
    path('blog-update/<int:pk>', update_blog, name='blog-update'),
    path('blog-delete/<int:pk>', delete_blog, name='blog-delete'),
]

urlpatterns += router.urls
