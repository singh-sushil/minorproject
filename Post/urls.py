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
    path("post_detail_authenticated/", views.PostDetailAuthenticatedView.as_view(), name="post_detail_authenticated"),
    path("post_detail_outside/", views.PostDetailOutsideView.as_view(), name="post_detail_outside"),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path("khalti-request/",views.KhaltiRequestView.as_view(),name="khaltirequest"),
    path("khalti-verify/",views.KhaltiVerifyView.as_view(),name="khaltiverify"),
    path('Illam/', views.Post_List_Illam.as_view(),name='illam'),
    path('Jhapa/', views.Post_List_Jhapa.as_view(),name='jhapa'),
    path('Saptari/', views.Post_List_Saptari.as_view(),name='saptari'),
    path('Siraha/', views.Post_List_Siraha.as_view(),name='siraha'),
    path('Chitwan/', views.Post_List_Chitwan.as_view(),name='chitwan'),
    path('Kathmandu/', views.Post_List_Kathmandu.as_view(),name='kathmandu'),
    path('Kaski/', views.Post_List_Kaski.as_view(), name='kaski'),
    path('Tanahun/', views.Post_List_Tanahun.as_view(), name='tanahun'),
    path('Palpa/', views.Post_List_Palpa.as_view(), name='palpa'),
    path('Rupendehi/', views.Post_List_Rupendehi.as_view(), name='rupendehi'),
    path('Dolpa/', views.Post_List_Dolpa.as_view(), name='dolpa'),
    path('Humla/', views.Post_List_Humla.as_view(),name='humla'),
    path('Darchula/', views.Post_List_Darchula.as_view(), name='darchula'),
    path('Kailali/', views.Post_List_Kailali.as_view(), name='kailali'),
    
]
