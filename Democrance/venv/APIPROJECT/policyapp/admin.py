from django.contrib import admin
from .models.customer import Customer
from .models.policy import Policy
from .models.policy_list import  Policylist
#from .models.policy_details import policydetails


class Admincustomer(admin.ModelAdmin):
    
    list_display=['first_name','last_name','dob']

class AdminPolicy(admin.ModelAdmin):
    list_display=['type','customer','premium','state']

class AdminPolicylist(admin.ModelAdmin):
    list_display=['policyname']



# Register your models here.
admin.site.register(Customer,Admincustomer)
admin.site.register(Policy,AdminPolicy)
admin.site.register(Policylist,AdminPolicylist)
#admin.site.register(policydetails)