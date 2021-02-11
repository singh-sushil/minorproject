from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import UserCreateForm


class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy("accounts:login")
    template_name = "signup.html"


class Profile(TemplateView):
    template_name = 'profile.html'

class MorangView(TemplateView):
    template_name = 'morang.html'

class MorangDetailView(TemplateView):
    template_name = 'morang1details.html'
'''
class UserInfo:
    def __init__(self,request):
        return request.user.id
'''

    
