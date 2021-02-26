'''from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)


class Homepage(TemplateView):
    template_name = 'homepage.html'
'''
from django.shortcuts import render
def HomePage(request):
    print(request.user.id)
    return render(request,'homepage.html',{'uid':request.user.id})