from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.http import HttpResponse, request




def myindex(request):
	return render(request, 'index/index.html')

def mymarket(request):
	return render(request, 'index/how-it-works.html')

def mycus(request):
	return render(request, 'index/faqs.html')
def myabout(request):
	return render(request, 'index/about.html')
def mypri(request):
	context = {}
	return render(request, 'acc/privacy-policy.html',context)
def myhelp(request):
	context = {}
	return render(request, 'acc/terms.html',context)


def mycontact(request):
	if request.method == 'POST':
		form = Contactform(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Thanks for your message we will repyl you shortly')
			
	else:
		form = Contactform()
	return render(request, 'index/contact.html')
