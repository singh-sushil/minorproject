from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import UserCreateForm


class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy("accounts:login")
    template_name = "signup.html"


class Profile(TemplateView):
    template_name = 'index.html'

class MorangView(TemplateView):
    template_name = 'morang.html'