from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)


class Homepage(TemplateView):
    template_name = 'homepage.html'
