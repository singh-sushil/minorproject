from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView
from django.urls import reverse, reverse_lazy
from .models import Post
from .forms import PostForm


class PostFormView(View):
    form_class = PostForm
    initial = {'key': 'value'}
    template_name = 'post_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            # return HttpResponseRedirect(reverse_lazy('post:image_display', kwargs={'pk': obj.id}))
            return redirect('/post/success/')
        return render(request, self.template_name, {'form': form})


class ImageDisplay(DetailView):
    model = Post
    template_name = 'image_display.html'
    context_object_name = 'abc'


class Post_List(ListView):
    model = Post
    template_name = 'post_list.html'


class PostSuccess(TemplateView):
    template_name = 'post_success.html'
