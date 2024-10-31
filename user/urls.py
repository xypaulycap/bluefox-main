
from django.urls import path
from . import views
from .views import *
app_name='userurl'
urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signupView, name='signup'),
    path('login/', views.loginView, name='login'),

    path('profit-history', views.profit, name="profit"),
    path('logout/', views.logout_view, name='logout'),
    path('kyc/', views.kyc, name='kyc'),
    path('my-trades/', views.trade_log, name='my_trades'),
    path('my-withdraws/',views.withdraw_log, name='withdraws'),
    path('deposit/', views.fund, name='depo'),
    path('market/', views.mymarket, name='market'),
    path('payments/<slug>/', views.myfund, name='payment'),
    path('copy-trader/<slug>/', views.mycopyp, name='copytraders'),
 
    path('wallets/',views.wallet, name='wallets'),
    path('copy-trade/',views.copytr, name='copy'),
    path('subscribe/',views.mysub, name='sub'),
    path('downlines/',views.banwithdrawal, name='down'),
    path('my-demo/',views.demo, name='demo'),

    path('my-dashboard/',views.myacc, name='dash'),
    
    path('copy-trades/', views.trade, name='trade'),
    path('trade-week/<slug>/', views.exe, name='ex'),
    path('withdrawal/', views.withdrawal, name='withal'),
    path('mykyc/', views.mykyc, name='banwith'),
    path('mydeposit/', views.mypro, name='mydeposit'),
    path('deposit/', views.fund, name='depo'),
    path('plan/', views.plan, name='plan'),
    path('my-plan/', views.myinvest, name='my-plan'),
    path('otp', views.reotp, name='otp'),
    path('activate-user/<uidb64>/<token>', views.activate_user, name='activate'),
    path('change_password/', views.change_password, name='change_password'),
	path('change_password_confirm/', views.change_password_confirm, name='change_password_confirm'),
	path('<slug:pk>', views.change_password_code, name='change_password_code'),
	path('change_password_success/', views.change_password_success, name='change_password_success'),
 
   

    
]