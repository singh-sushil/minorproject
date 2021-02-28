from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
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
            p = Post()
            data = form.cleaned_data
            p.province = request.POST.get('province')
            p.district = request.POST.get('district')
            p.owners_name=data['owners_name']
            p.Address=data['Address']
            p.contact_number=data['contact_number']
            p.location=data['location']
            p.amount=data['amount']
            p.length=data['length']
            p.Area=data['Area']
            p.image1=data['image1']
            p.image2=data['image2']
            p.image3=data['image3']
            p.image4 = data['image4']
            p.payment_verification_slip = data['payment_verification_slip']
            p.save()
            return redirect('/post/success/')
        return render(request, self.template_name, {'form': form})


class ImageDisplay(DetailView):
    model = Post
    template_name = 'image_display.html'
    context_object_name = 'abc'


class Post_List_outside(ListView):
    model = Post
    template_name = 'post_list_outside.html'
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class Post_List_authenticated(ListView):
    model=Post
    template_name='post_list_authenticated.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailAuthenticatedView(ListView):
    model = Post
    template_name = 'postdetailauthenticated.html'   

class PostDetailOutsideView(ListView):
    model = Post
    template_name = 'postdetailoutside.html'  

class PostSuccess(TemplateView):
    template_name = 'post_success.html'


class DraftListView(ListView):
    model = Post
    template_name = 'post_draft_list.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post:post_list_authenticated')

class KhaltiRequestView(View):
    def get(self,request,*args,**kwargs):
        context={

        }
        return render(request,"khaltirequest.html",context)

class KhaltiVerifyView(View):
    def get(self,request,*args,**kwargs):
        data={}
        return JsonResponse(data)

