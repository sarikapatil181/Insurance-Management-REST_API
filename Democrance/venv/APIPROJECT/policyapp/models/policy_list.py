from django.db import models
from .customer import Customer
#from .policy import Policy

#policylist with list of policy
class Policylist(models.Model):
    policyname=models.CharField(max_length=50)
  
    #policy=models.ForeignKey(Policy,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.policyname

    