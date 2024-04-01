from django.urls import path


from .views import home, create_blog, detail_blog, edit_blog

from .views_cbv import CreateBlogView, HomePageView
app_name = 'app'

urlpatterns = [
    path('blog/<int:id>', detail_blog, name='detail'),
    path('blog/<slug:slug>', edit_blog, name='edit'),
]

urlpatterns_cbv = [
    path('home/', HomePageView.as_view(), name='home'),
    path('create/', CreateBlogView.as_view(), name='create'),
]
urlpatterns += urlpatterns_cbv
