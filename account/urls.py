from django.urls import path
from account.views import login_view, SignUpView, logout_view, profile_view

app_name = 'account'

urlpatterns = [
    path('', login_view, name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
]
