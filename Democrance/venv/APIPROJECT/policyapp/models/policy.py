from  django.db import models
from .customer import Customer
from .policy_list import Policylist

#Policy model with cutomer_id as a foreign key
class Policy(models.Model):
    policystatus=(
    ('new', ("new")),
    ('quoted', ("quoted")),
    ('active',("active")),
    ('accepted',("accepted")),
    ('bound',("bound"))
)
    type=models.CharField(max_length=50)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,default=1)
    policy=models.ForeignKey(Policylist,on_delete=models.CASCADE,default=1)
    premium=models.IntegerField()
    cover=models.CharField(max_length=50)
    state=models.CharField(max_length=50,choices=policystatus)
    def __str__(self):
        return self.type
    @property
    def cust_id(self):
        return self.customer.id

'''def get_policy_by_cust_id(id):
    return Customer.objects.filter(cust_id=id)'''
