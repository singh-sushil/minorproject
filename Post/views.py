from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView
from django.urls import reverse, reverse_lazy
from .models import Post
from .forms import PostForm
from django.utils import timezone

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

class Post_List(ListView):
    model = Post
    template_name = 'post_list.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostSuccess(TemplateView):
    template_name = 'post_success.html'


class DraftListView(ListView):
    model = Post
    template_name='post_draft_list.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')

class PostDetailView(DetailView):
    model=Post
    template_name='post_detail.html'


def post_publish(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post:post_list')
