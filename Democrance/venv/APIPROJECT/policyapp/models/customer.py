from django.db import models

'''
class Customer1(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    dob=models.DateField()
'''
#customer Model for customer registration
class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    dob=models.DateField()
    def __str__(self):
        return self.first_name
    
'''def get_customers_by_name(name):
    return Customer.objects.filter(first_name=name) 
    
def   get_customers_by_name():
    return Customer.objects.all()'''


    