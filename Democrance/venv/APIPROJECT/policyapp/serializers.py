from .models import *
from rest_framework import serializers
from .models.policy_list import Policylist
from .models.policy import Policy
#serilizer class for customer model
class CustomerSerializer(serializers.Serializer):
    first_name=serializers.CharField(max_length=50)
    last_name=serializers.CharField(max_length=50)
    dob=serializers.DateField()
    def create(self,validated_data):
       #print("serilizer created")
       return Customer.objects.create(**validated_data)
#serilizer class for Policy model
class PolicyS(serializers.Serializer):
    
    type=serializers.CharField(max_length=50)
    #customer=models.ForeignKey(Customer,on_delete=models.CASCADE,default=1)
    premium=serializers.IntegerField()
    cover=serializers.CharField(max_length=50)
    state=serializers.CharField(max_length=50)
    cust_id=serializers.ReadOnlyField()
    class Meta:
        model=Policy
    def create(self,validated_data):
       #print("serilizer created")
       return Policy.objects.create(**validated_data)
#serilizer class for policy list model
class policylistS(serializers.Serializer):
    policyname=serializers.CharField(max_length=50)
    cust_id=serializers.ReadOnlyField()
    class Meta:
        model=Policylist
    def create(self,validated_data):
       #print("serilizer created")
       return Policylist.objects.create(**validated_data)


'''class AcceptquoteSerializer(serializers.Serializer):
    #quote=models.ForeignKey(Quote,on_delete=models.CASCADE)
    status=serializers.CharField(max_length=30, default='accepted')
    quote_id=serializers.ReadOnlyField()

    def create(self,validated_data):
       #print("serilizer created")
       return Acceptquote.objects.create(**validated_data)

    class Meta:
        model=Acceptquote'''