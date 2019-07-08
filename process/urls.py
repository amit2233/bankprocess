from django.urls import path
from .views import *

urlpatterns = [
        path('process', ListProcess.as_view(), name='cust-add'),
        path('workflow', ListWorkFlow.as_view(), name='cust-add'),
        path('rules', ListRule.as_view(), name='cust-add'),   

]