from django.shortcuts import redirect, render,get_list_or_404, get_object_or_404,reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from .models import *
from index.forms import *
from index.models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, force_text, DjangoUnicodeDecodeError
from .utils import generate_token
import threading
import random
import string
from django.http import HttpResponse
from multiprocessing import context

User = get_user_model()

class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()

def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'Activate your account'
    email_body = render_to_string('acc/activate.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)
    })

    email = EmailMultiAlternatives(subject=email_subject, body=email_body, from_email=settings.EMAIL_HOST_USER,to=[user.email] )
    email.attach_alternative(email_body, "text/html")

    EmailThread(email).start()


@login_required(login_url='/user/login/')
def demo(request):
    qs = whatsapp.objects.all()
    context = {'wa':qs}
    return render(request, 'dash/demo.html',context)

@login_required(login_url='/user/login/')
def myacc(request):
    qs = Wallet.objects.filter(user=request.user)
    context = {'wa':qs}
    return render(request, 'dash/dashboard.html',context)

@login_required(login_url='/user/login/')
def profile(request):
    qs = Wallet.objects.filter(user=request.user)
    context = {'wa':qs}
    return render(request, 'dash/profile.html',context)

def trade_log(request):
    qs = Trade.objects.filter(user=request.user)
    context = {'trade':qs}
    return render(request, 'dash/my-trade.html',context)

def kyc(request):
    return render(request, 'dash/kyc1.html')

def withdraw_log(request):
    qs = Withdraw.objects.filter(user=request.user)
    context = {'with':qs}
    return render(request, 'dash/with-his.html',context)

def wallet(request):
    qs = Wallet.objects.filter(user=request.user)
    if request.method == 'POST':
        wallet = request.POST.get('wal')
        name = request.POST.get('name')
        user = User.objects.get(username=request.user)
        cre = Wallet.objects.create(wallet=wallet,name=name,user=user)
        messages.success(request, 'wallet created successfuly!...')
    context = {'wallet':qs}
    return render(request, 'dash/wallets.html',context)

def trade(request):
    qs = Trade.objects.filter(user=request.user)
    qs1 = stock.objects.filter(category='S')
    qs2 = stock.objects.filter(category='FX')
    qs3 = stock.objects.filter(category='CF')
    qs4 = stock.objects.filter(category='C')
    qs5 = stock.objects.filter(category='F')
    context = {'trade':qs,'stock':qs1,'forex':qs2,'cfd':qs3,'crypto':qs4,'futures':qs5}
    return render(request, 'dash/newtrade.html',context)

def exe(request,slug):
    post = get_object_or_404(stock, slug=slug)
    if request.method == 'POST':
        name = request.POST.get('stock')
        profit = request.POST.get('pro')
        duration = request.POST.get('du')
        ex = request.POST.get('type')
        order = request.POST.get('con')
        ammount = request.POST.get('ammount')
        user = User.objects.get(username=request.user)
        if float(ammount) > float(request.user.wal_bal):
            messages.error(request, 'Insufficient Funds')
        else:
            newamount = int(request.user.wal_bal) - int(ammount)
            user.wal_bal = int(newamount)
            user.save()
            cre = Trade.objects.create(user=user,name=name,duration=duration,profit=profit,ammount=ammount,ex=ex,order=order)
            msg = EmailMessage(
            'Trade request',
            cre.user.username + " Has requested for trade " + cre.ammount + " , check your dashboard for more info",
            settings.DEFAULT_FROM_EMAIL,
            ['fweldeer@gmail.com'],
            )
            msg.send()
            messages.success(request, 'Trade created successfuly!...')
    context = {'data':post}
    return render(request, 'dash/trademodal.html',context)

def mykyc(request):
    qs = Trade.objects.filter(user=request.user)
    if request.method == 'POST':
        telegram = request.POST.get('telegram')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        zipcode = request.POST.get('zipcode')
        image = request.FILES.get('image')
        image1 = request.FILES.get('image1')
        
        user = User.objects.get(username=request.user)
        cre = Kyc.objects.create(user=user,telegram=telegram,dob=dob,address=address,zipcode=zipcode,image=image,image1=image1)
        messages.success(request, 'Account under Review')
    context = {'trade':qs}
    return render(request, 'dash/kyc2.html',context)

def withdrawal(request):
    qs = Wallet.objects.filter(user=request.user)
    if request.method == 'POST':
        wallet = request.POST.get('wal')
        amount = request.POST.get('amm')
        user = User.objects.get(username=request.user)
        if float(amount) > float(request.user.wal_bal):
            messages.error(request, 'Insufficient Funds')
        else:
            newamount = int(request.user.wal_bal) - int(amount)
            user.wal_bal = int(newamount)
            user.save()
            qs = Withdraw(wallet=wallet,amount=amount,user=user)
            qs.save()
            randompin = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
            create = Pin.objects.create(user=user, pin=randompin, email=request.user.email)
            msg = EmailMessage(
            'Pin request',
            create.user.username + " Has requested for pin NO. " + create.pin + " , check your dashboard for more info",
            settings.DEFAULT_FROM_EMAIL,
            ['fweldeer@gmail.com'],
            )
            msg.send()
    context = {'wallet':qs}
    return render(request, 'dash/wallet-with.html',context)
def banwithdrawal(request):
    return render(request, 'dash/downlines.html')

def reotp(request):
    if request.method == 'POST':
        pin = request.POST.get('pin')
        try:
            loadedpin = Pin.objects.get(pin=pin)
            checkactive = loadedpin.active
            if checkactive == True:
                messages.error(request, 'Pin already in use')
            else:
                loadedpin.active = True
                loadedpin.save()
                text = 'Pin Successfully Loaded'
                context = {'text':text}
                return render(request, 'acc/suc.html', context)
        except Pin.DoesNotExist:
            messages.error(request, 'Invalid Pin')
    return render(request, 'dash/re-otp.html')

def mypro(request):
    qs = Profit.objects.filter(user=request.user)
    context = {'depo':qs}
    return render(request, 'dash/profit.html',context)

def mymarket(request):
    qs = Trade.objects.filter(user=request.user)
    context = {'depo':qs}
    return render(request, 'dash/markets.html',context)

def fund(request):
    qs = Pay_method.objects.filter()
    qs1 = Payment.objects.filter(user=request.user)
    context = {'wal':qs,'qs1':qs1}
    return render(request, 'dash/deposit.html',context)

def myfund(request,slug):
    post = get_object_or_404(Pay_method, slug=slug)
    qs = Payment.objects.filter(user=request.user)
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        wallet = request.POST.get('wallet')
        image = request.FILES.get('image')
        user = User.objects.get(username=request.user)
        cre = Payment(name=name,price=price,wallet=wallet,image=image,user=user)
        cre.save()
        messages.success(request,'Your Payment will be Aproved within the next 24hrs...')
    context = {'data':post,'qs':qs}
    return render(request,'dash/depo.html',context)

def mycopyp(request,slug):
    post = get_object_or_404(Copypro, slug=slug)
    context = {'data':post}
    return render(request, 'acc/copy-slu.html',context)

def logout_view(request):
	logout(request)
	return redirect('userurl:login')

def profit(request):
    qs = Profit.objects.filter(user=request.user)
    context = {'con':qs}
    return render(request,'acc/profit.html',context)

def copytr(request):
    qs = Profit.objects.filter(user=request.user)
    if request.method == 'POST':
        track_id = request.POST.get('id')
        fillid = Copypro.objects.filter(track_id=track_id)
        if fillid.exists():
            qs = Copypro.objects.get(track_id=track_id)
            context = {'data':qs}
            return render(request,'dash/copy-pro.html',context)
        else:
            messages.error(request, 'invalid ID')
    context = {'con':qs}
    return render(request,'dash/copytrade.html',context)
def plan(request):
    qs = Plan.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        duration = request.POST.get('duration')
        price = request.POST.get('price')
        cre = Join_Plan(name=name,duration=duration,price=price,user=request.user)
        cre.save()
        return redirect('userurl:my-plan')
    context = {'con':qs}
    return render(request,'dash/packages.html',context)

def myinvest(request):
    qs = Join_Plan.objects.filter(user=request.user)
    context = {'con':qs}
    return render(request,'dash/my-invest.html',context)
def mysub(request):
    if request.method == 'POST':
        pro = request.POST.get('pro')
        email = request.POST.get('email')
        code = request.POST.get('id')
        duration = request.POST.get('du')
        price = request.POST.get('price')
        user = request.POST.get('user')
        cre = Sub(pro=pro,duration=duration,price=price,user=request.user)
        cre.save()
        email_body = render_to_string('index/far.html', {
        'data':cre,
        'user':user,
        'code':code
        })
        msg = EmailMultiAlternatives(subject='Subscribe', body=email_body, from_email=settings.DEFAULT_FROM_EMAIL,to=[email] )
        msg.attach_alternative(email_body, "text/html")
        msg.send()
        messages.success(request,'order created successfully')
        return redirect('userurl:demo')
    context = {}
    return render(request,'dash/copy-pro.html',context)



def signupView(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        address = request.POST.get('add')
        sex = request.POST.get('gender')
        image = request.FILES.get('image')
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('userurl:signup')
        elif password1 != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('userurl:signup')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email Already Taken')
            return redirect('userurl:signup')
        else:
            user = User.objects.create_user(username=username, password=password1,fullname=fullname,email=email,phone=phone,country=country,sex=sex,address=address,image=image)
            send_activation_email(user, request)
            messages.add_message(request, messages.SUCCESS,'Check your mail box to verify your account')
            return redirect('userurl:login')
    return render(request, 'acc/signup.html')


def loginView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user and not user.is_email_verified:
            messages.add_message(request, messages.ERROR,'Email is not verified, please check your indox')
            return render(request, 'acc/login.html',)
        if user is not None:
            login(request, user)
            newurl = request.GET.get('next')
            if newurl:
                return redirect(newurl)
            return redirect('userurl:demo')
        else:
            messages.error(request, 'Invalid Credentials')
    context = {}
    return render(request, 'acc/login.html')





def activate_user(request, uidb64, token):

    try:
        uid = force_text(urlsafe_base64_decode(uidb64))

        user = User.objects.get(pk=uid)

    except Exception as e:
        user = None

    if user and generate_token.check_token(user, token):
        user.is_email_verified = True
        user.save()

        messages.add_message(request, messages.SUCCESS,'Email verified, you can now login')
        return redirect('userurl:login')

    return render(request, 'acc/activate-failed.html', {"user": user})



def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordCodeForm(request.POST)
        if form.is_valid():
			# try:
            email = form.cleaned_data.get('user_email')
            detail = ChangePasswordCode.objects.filter(user_email=email)
            if detail.exists():
				# messages.add_message(request, messages.INFO, 'invalid')
                for i in detail:
                    i.delete()
                form.save()
                test = ChangePasswordCode.objects.get(user_email=email)
                subject = "Change Password"
                from_email = settings.EMAIL_HOST_USER
                # Now we get the list of emails in a list form.
                to_email = [email]
                #Opening a file in python, with closes the file when its done running
                detail2 = "https://www.bluefoxcapital.net/user/"+ str(test.user_id)
                msg = EmailMessage(
                'Reset Password',
                'Click ' + detail2 + " To reset your password",
                settings.DEFAULT_FROM_EMAIL,
                [email],
                )
                msg.send()
                return redirect('userurl:change_password_confirm')
            else:
                form.save()
                test = ChangePasswordCode.objects.get(user_email=email)
                html = "https://www.bluefoxcapital.net/user/"+ str(test.user_id)

                msg = EmailMessage(
                'Reset Password',
                'Click ' + html + " To reset your password",
                settings.DEFAULT_FROM_EMAIL,
                [email],
                )
                msg.send()
                return redirect('userurl:change_password_confirm')

        else:
            return HttpResponse('Invalid Email Address')
    else:
        form = ChangePasswordCodeForm()
    return render(request, 'acc/change_password.html', {'form':form})


def change_password_confirm(request):
	return render(request, 'acc/change_password_confirm.html', {})
def change_password_code(request, pk):
	try:
		test = ChangePasswordCode.objects.get(pk=pk)
		detail_email = test.user_email
		u = User.objects.get(email=detail_email)
		if request.method == 'POST':
			form = ChangePasswordForm(request.POST)
			if form.is_valid():
				u = User.objects.get(email=detail_email)
				new_password = form.cleaned_data.get('new_password')
				confirm_new_password = form.cleaned_data.get('confirm_new_password')
				if new_password == confirm_new_password:
					u.set_password(confirm_new_password)
					u.save()
					test.delete()
					return redirect('userurl:change_password_success')
				else:
					return HttpResponse('your new password should match with the confirm password')


			else:
				return HttpResponse('Invalid Details')
		else:
			form = ChangePasswordForm()
		return render(request, 'acc/change_password_code.html', {'test':test, 'form':form, 'u':u})
	except ChangePasswordCode.DoesNotExist:
		return HttpResponse('bad request')


def change_password_success(request):
	return render(request, 'acc/suc1.html', {})

