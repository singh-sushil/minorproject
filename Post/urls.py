from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'post'
urlpatterns = [
    path('postform/', views.PostFormView.as_view(), name='postform'),
    path('post_list/', views.Post_List.as_view(), name='post_list'),
    path('image_display/', views.ImageDisplay.as_view(), name='image_display'),
    path('success/', views.PostSuccess.as_view(), name='postsuccess'),
    path("post_detail/", views.PostDetailView.as_view(), name="post_detail"),

]
