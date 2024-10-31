from django.urls import path
from . import views

app_name = 'indexurl'
urlpatterns = [
	path('', views.myindex, name='index'),
	path('markets/',  views.mymarket ,name='market'),
	path('customers/',  views.mycus ,name='cus'),
	path('about-us/',  views.myabout ,name='about'),
	path('contact/',  views.mycontact ,name='contact'),
	path('terms/',  views.myhelp ,name='terms'),
	path('privacy-policy/',  views.mypri ,name='privacy'),
	


    ]

