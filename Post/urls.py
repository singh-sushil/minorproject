from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'post'
urlpatterns = [
    path('postform/', views.PostFormView.as_view(), name='postform'),
    path('post_list_outside/', views.Post_List_outside.as_view(), name='post_list_outside'),
    path('post_list_authenticated/', views.Post_List_authenticated.as_view(), name='post_list_authenticated'),
    path('image_display/', views.ImageDisplay.as_view(), name='image_display'),
    path('success/', views.PostSuccess.as_view(), name='postsuccess'),
    path("post_detail/", views.PostDetailView.as_view(), name="post_detail"),
    path("khalti-request/",views.KhaltiRequestView.as_view(),name="khaltirequest"),
    path("khalti-verify",views.KhaltiVerifyView.as_view(),name="khaltiverify"),
    
    
]
