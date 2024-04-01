from django.shortcuts import render
from django.views.generic import CreateView
from django.shortcuts import redirect, reverse
from django.contrib.auth import authenticate, login, logout
from account.forms import User, LoginForm
from account.forms import SignUpForm


class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'account/sign_up.html'
    success_url = '/home'


def login_view(request):
    # form = LoginForm
    if request.method == "POST":
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(request, phone=phone, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('app:home'))

    return render(request, 'account/login.html')


def logout_view(request):
    logout(request)
    return redirect(reverse('account:login'))


def profile_view(request):
    pass

