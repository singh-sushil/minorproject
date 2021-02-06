from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import FeedbackForm
from django.views.generic import TemplateView, ListView
from django.urls import reverse
from .models import Rateapp, Feedback


class MyFormView(View):
    form_class = FeedbackForm
    initial = {'key': 'value'}
    template_name = 'form_template.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid() and request.POST.get('rateapp'):
            form.save()
            r_app = Rateapp()
            r_app.rateapp = request.POST.get('rateapp')
            r_app.save()
            return redirect('/feedback/thankyou/')
        return render(request, self.template_name, {'form': form})


class Feedback_List(ListView):
    model = Feedback
    template_name = 'feedback_list.html'


class Thankyou(TemplateView):
    template_name = 'thankyou.html'
