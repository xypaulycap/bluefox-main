from django.contrib import admin
from .models import *



class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username',  'email']
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user',  'approve']

class PinAdmin(admin.ModelAdmin):
    list_display = ['pin','user',  'active','time']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Plan)
admin.site.register(Trade)
admin.site.register(stock)
admin.site.register(Pin,PinAdmin)
admin.site.register(Withdraw)
admin.site.register(Profit)
admin.site.register(Join_Plan)
admin.site.register(Pay_method)
admin.site.register(Copypro)
admin.site.register(Sub)
admin.site.register(Payment,PaymentAdmin)