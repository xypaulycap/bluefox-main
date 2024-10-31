from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.text import slugify
from django.contrib.auth import get_user_model
import uuid


class CustomUser(AbstractUser):
    fullname = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=50, default='')
    country = models.CharField(max_length=50,default='0')
    sex = models.CharField(max_length=50,default='0')
    address = models.CharField(max_length=50,default='0')
    active_inv = models.CharField(max_length=50,default='0')
    active_trade = models.CharField(max_length=50,default='0')
    copier = models.CharField(max_length=50,default='0')
    wal_bal = models.CharField(max_length=50,default='0')
    demon = models.CharField(max_length=50,default='10,000')
    btc = models.CharField(max_length=50,default='0.00',blank=True)
    image = models.FileField(default='https://res.cloudinary.com/danmybn7o/image/upload/v1649117194/media_cdn/pro_neycaw.png',blank=True)
    is_email_verified = models.BooleanField(default=False)
    def __str__(self):
        return self.username

class Kyc(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    telegram = models.CharField(max_length=50, default='')
    address = models.CharField(max_length=50, default='')
    zipcode = models.CharField(max_length=50,default='0')
    dob = models.CharField(max_length=50,default='0')
    image = models.FileField()
    image1 = models.FileField()
    
    def __str__(self):
        return self.telegram
class stock(models.Model):
    CATEGORY_CHOICES = (
    ('C', 'Crypto'),
    ('F', 'Futures'),
    ('CF', 'Cfd'),
    ('S', 'Stocks'),
    ('FX', 'Forex')
   
)

    name = models.CharField(max_length=50, default='')
    link = models.CharField(max_length=50, default='')
    slug = models.SlugField(blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10 ,null=True)

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(stock, self).save(*args, **kwargs)

class Plan(models.Model):
    name = models.CharField(max_length=50,default='0')
    profit = models.CharField(max_length=50,default='0')
    mindeposit = models.CharField(max_length=50,default='0')
    maxdeposit = models.CharField(max_length=50,default='0')
    ref = models.CharField(max_length=50,default='0')
    days = models.CharField(max_length=50,default='0')
    def __str__(self):
        return self.name

class Trade(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=50,default='0')
    profit = models.CharField(max_length=50,default='0')
    duration = models.CharField(max_length=50,default='0')
    ex = models.CharField(max_length=50,default='0')
    order = models.CharField(max_length=50,default='0')
    ammount = models.CharField(max_length=50,default='0')
    approve = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True,null=True,blank=True,)
    msg = models.CharField(max_length=50,default='Running')
    total = models.CharField(max_length=50,default='-----')
    def __str__(self):
        return self.name
        
class Wallet(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=20,default='0')
    wallet = models.CharField(max_length=50,default='0')
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username

class Profit(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    ammount = models.CharField(max_length=50,default='0')
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username
class Join_Plan(models.Model):
    name = models.CharField(max_length=50,default='0')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    price = models.CharField(max_length=50,default='0')
    duration = models.CharField(max_length=50,default='0')
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user

class Pay_method(models.Model):
    name = models.CharField(max_length=50,default='0')
    wallet = models.CharField(max_length=500,default='0')
    image = models.FileField()
    visible = models.BooleanField(default=True)
    slug = models.SlugField(blank=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Pay_method, self).save(*args, **kwargs)

class Payment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=50,default='0')
    price = models.CharField(max_length=50,default='0')
    wallet = models.CharField(max_length=500,default='0')
    image = models.FileField()
    approve = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Pin(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    pin = models.CharField(max_length=30, unique=True, blank=True)
    email = models.CharField(max_length=100, default='')
    active = models.BooleanField(default=False)
    approved = models.BooleanField(default=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    def __str__(self):
        return self.pin
class Withdraw(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    amount = models.CharField(max_length=30, blank=True)
    wallet = models.CharField(max_length=100, default='')
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username

class ChangePasswordCode(models.Model):
	user_email = models.EmailField(max_length=50)
	user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class ChangePassword(models.Model):
	new_password = models.CharField(max_length=50, blank = False, null = False)
	confirm_new_password = models.CharField(max_length=50, blank = False, null = False)

class Copypro(models.Model):
    fullname = models.CharField(max_length=200)
    my_equity = models.CharField(max_length=200)
    to_equity = models.CharField(max_length=200)
    profit = models.CharField(max_length=200,blank=True)
    loss = models.CharField(max_length=200)
    track_id = models.CharField(max_length=10, default='0')
    risk = models.CharField(default='0',max_length=20)
    min = models.CharField(default='0',max_length=20)
    copiers = models.CharField(default='0',max_length=20)
    image = models.ImageField(default='pro.jpg')
    join = models.DateTimeField(auto_now_add=False,blank=True)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.fullname)
        super(Copypro, self).save(*args, **kwargs)
    

    def __str__ (self):
        return self.fullname


class Sub(models.Model):
    pro = models.CharField(max_length=50,default='0')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    price = models.CharField(max_length=50,default='0')
    duration = models.CharField(max_length=50,default='0')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.pro
