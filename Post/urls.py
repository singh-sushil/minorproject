from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'post'
urlpatterns = [
    path('postform/', views.PostFormView.as_view(), name='postform'),
    path('post_list/', views.Post_List.as_view(), name='post_list'),
    path('success/', views.PostSuccess.as_view(), name='postsuccess'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('detail/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
]
