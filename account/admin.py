from django.contrib import admin
from .models import account

# Register your models here.
class admin_account(admin.ModelAdmin):
    list_display = ['ID','First_Name','Middle_Name','Last_name','Date_of_Birth','Age','Email','AdharCard']

admin.site.register(account,admin_account)
#admin.site.register(LoanApplicationModel,LoanAdmin)
