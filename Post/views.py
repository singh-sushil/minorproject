from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
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
            # pm=form.cleaned_data.get("payment_method")
            # if pm=="Khalti":
            #     return redirect(reverse("post:khaltirequest"))
            return redirect('/post/success/')
        return render(request, self.template_name, {'form': form})


class ImageDisplay(DetailView):
    model = Post
    template_name = 'image_display.html'
    context_object_name = 'abc'


class Post_List_outside(ListView):
    model = Post
    template_name = 'post_list_outside.html'

class Post_List_authenticated(ListView):
    model=Post
    template_name='post_list_authenticated.html'

class PostDetailAuthenticatedView(ListView):
    model = Post
    template_name = 'postdetailauthenticated.html'   

class PostDetailOutsideView(ListView):
    model = Post
    template_name = 'postdetailoutside.html'  

class PostSuccess(TemplateView):
    template_name = 'post_success.html'

class KhaltiRequestView(View):
    def get(self,request,*args,**kwargs):
        context={

        }
        return render(request,"khaltirequest.html",context)

class KhaltiVerifyView(View):
    def get(self,request,*args,**kwargs):
        data={}
        return JsonResponse(data)

