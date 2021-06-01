from django.contrib import admin
from django.urls import path,include
from .views import index
from .views import CustomerViewSet
from .views import PolicyViewSet
from rest_framework.routers import DefaultRouter
from .views import  PolicylistViewSet, CustomerAPIView,PolicyAPIView



#url for policyapp..this url file is included in mainproject urls.py using include

router =DefaultRouter()
router.register('create_customer', CustomerViewSet, basename='customer')#create customer api
router.register('quote',PolicyViewSet,basename='quote')#quote api to see policy details with customer id
router.register('policy',PolicylistViewSet,basename='policyname')#api to see list of policies

urlpatterns = [
    
    path('',index),
    
    path('api/v1/',include(router.urls)),
    #Search functionality for customer model
    path('customer/',CustomerAPIView.as_view()),
    #search functionality based on customer and policy details   
    path('policy/',PolicyAPIView.as_view())
   
]