from django.urls import path
from  .import views

urlpatterns = [
    path('', views.index, name='all-meetups'),  #localhost/meetups
    path('<slug:meetup_id>/success', views.confirm_registration, name='confirmation'),
    path('<slug:meetup_id>', views.meetup_details, name='meetup-detail')  #localhost/meetups
    
]


