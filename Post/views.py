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
            p.frontview=data['frontview']
            p.leftsideview=data['leftsideview']
            p.backsideview=data['backsideview']
            p.rightsideview = data['rightsideview']
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


class Post_List_Illam(ListView):
    model = Post
    template_name = 'illam.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).filter(district="Illam").order_by('-published_date')


class Post_List_Jhapa(ListView):
    model = Post
    template_name = 'jhapa.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).filter(district="Jhapa").order_by('-published_date')


class Post_List_Saptari(ListView):
    model = Post
    template_name = 'saptari.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).filter(district="Saptari").order_by('-published_date')

class Post_List_Siraha(ListView):
    model = Post
    template_name = 'siraha.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).filter(district="Siraha").order_by('-published_date')


class Post_List_Chitwan(ListView):
    model = Post
    template_name = 'chitwan.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).filter(district="Chitwan").order_by('-published_date')


class Post_List_Kathmandu(ListView):
    model = Post
    template_name = 'kathmandu.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).filter(district="Kathmandu").order_by('-published_date')


class Post_List_Kaski(ListView):
    model = Post
    template_name = 'kaski.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).filter(district="Kaski").order_by('-published_date')


class Post_List_Tanahun(ListView):
    model = Post
    template_name = 'tanahun.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).filter(district="Tanahun").order_by('-published_date')


class Post_List_Palpa(ListView):
    model = Post
    template_name = 'palpa.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).filter(district="Palpa").order_by('-published_date')
    

class Post_List_Rupendehi(ListView):
    model = Post
    template_name = 'rupendehi.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).filter(district="Rupendehi").order_by('-published_date')


class Post_List_Dolpa(ListView):
    model = Post
    template_name = 'dolpa.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).filter(district="Dolpa").order_by('-published_date')

class Post_List_Humla(ListView):
    model = Post
    template_name = 'humla.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).filter(district="Humla").order_by('-published_date')


class Post_List_Darchula(ListView):
    model = Post
    template_name = 'darchula.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).filter(district="Darchula").order_by('-published_date')


class Post_List_Kailali(ListView):
    model = Post
    template_name = 'kailali.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).filter(district="Kailali").order_by('-published_date')
