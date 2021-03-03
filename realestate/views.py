'''from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)


class Homepage(TemplateView):
    template_name = 'homepage.html'
'''
from django.shortcuts import render
from Post.models import Post
from Post.forms import PostForm
from django.utils import timezone
# from django.db import connection as cn

data = Post.objects.filter(
    published_date__lte=timezone.now()).order_by('-published_date')
def HomePage(request):
    # cursor = cn.cursor()
    # q1 = "select * from post_post"
    # cursor.execute(q1)
    # data = cursor.fetchall()
    print(request.user.id)
    return render(request,'homepage.html',{'uid':request.user.id,'data':data})
