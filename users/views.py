import random
import secrets
import string

from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from users.models import User


class LoginView(BaseLoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        verification_code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        form.verification_code = verification_code
        user = form.save()
        user.verification_code = verification_code
        send_mail(
            subject='Подтверждение адреса электронной почты',
            message=f'ссылка для верификации: http://127.0.0.1:8000/users/verify?code={user.verification_code}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def verify(request):
    code = int(request.GET.get('code'))
    user = User.objects.get(verification_code=code)
    user.verified = True
    user.save()
    return render(request, 'users/verify.html')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(12))
    send_mail(
        subject='Смена пароля',
        message=f'Новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('users:login'))
