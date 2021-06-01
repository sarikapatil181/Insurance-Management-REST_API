from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import CustomerSerializer
from .serializers import PolicyS
from .serializers import policylistS
from rest_framework import generics,mixins
from .models.customer import Customer
from .models.policy import Policy
from .models.policy_list import Policylist
from rest_framework.viewsets import ViewSet, ModelViewSet
from django.views.generic.list import ListView
from rest_framework import filters

# Create your views here.
#client side
def index(request):
    return HttpResponse("<h1>Welcome</h1>")

    
'''class CustomerListView(generics.ListCreateAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer

class  PolicyListView(generics.ListCreateAPIView):
    queryset=Policy.objects.all()
    serializer_class=PolicyS'''

# Modelviewset for customer model   
class CustomerViewSet(ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer

#Modelviewset for policy model
class  PolicyViewSet(ModelViewSet):
    queryset=Policy.objects.all()
    serializer_class=PolicyS

#Modelviewset of list of policy
class  PolicylistViewSet(ModelViewSet):
    queryset=Policylist.objects.all()
    serializer_class=policylistS


#Search functionality using rest_framework based on cutomers first_name ,Last_name and dob.               
class CustomerAPIView(generics.ListCreateAPIView):
    search_fields = ['first_name','last_name','dob']
    filter_backends = (filters.SearchFilter,)
    queryset = Customer.objects.all()
    serializer_class =CustomerSerializer

#Search functionality using rest_framework based on policy details
class PolicyAPIView(generics.ListCreateAPIView):
     
    search_fields = ['id','state','premium']
    filter_backends = (filters.SearchFilter,)
    queryset = Policy.objects.all()
    serializer_class =PolicyS