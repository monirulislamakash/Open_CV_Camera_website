from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='home'),
    path('client_details/', views.client_details,name='client_details'),
    path('admin_page/', views.admin_page,name='admin_page'),
    path('delete/<int:id>/',views.delete,name="delete" ),
    path('login/', views.login,name='login'),
    path('singup/', views.singup,name='singup'),
    path('logout',views.logout,name="logout" ),

    path('video_feed', views.video_feed, name='video_feed'),
    path('webcam_feed', views.webcam_feed, name='webcam_feed'),
    #path('mask_feed', views.mask_feed, name='mask_feed'),
	path('livecam_feed', views.livecam_feed, name='livecam_feed'),
]