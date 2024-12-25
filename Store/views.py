from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth import login
from .models import Product
from .forms import UserRegisterForm, UserLoginForm

# домашняя страница
class HomePage(ListView):
    model = Product
    ordering = ['name']
    title = 'Fruit Store'
    template_name = 'home.html'

# регистрация
class RegisterView(FormView):
    form_class = UserRegisterForm
    template_name = 'Users/register.html'
    success_url = reverse_lazy('home')      # URL для перенаправления после успешной регистрации

    def form_valid(self, form):
        user = form.save()                  # Создаём нового пользователя
        login(self.request, user)           # Авторизуем пользователя
        return super().form_valid(form)
    
# Вход пользователя
class UserLoginView(LoginView):
    template_name = 'Users/login.html'
    form_class = UserLoginForm

    def get_success_url(self):
        return reverse_lazy('home')         # URL для перенаправления после успешного входа

# Выход пользователя
class UserLogoutView(LogoutView):
    #next_page = reverse_lazy('home')        # URL для перенаправления после выхода
    pass