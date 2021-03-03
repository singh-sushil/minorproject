from django.urls import path
from locationandfeedback import views

app_name = 'feedback'
urlpatterns = [
    path('myformview/', views.MyFormView.as_view(), name='myformview'),
    path('thankyou/', views.Thankyou.as_view(), name='thankyou'),
    path('feedback_list/', views.Feedback_List.as_view(), name='feedback_list'),
]
