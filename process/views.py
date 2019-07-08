# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializer import *
# Create your views here.


class ListProcess(generics.ListAPIView):
	queryset = Process.objects.all()
	serializer_class = ProcessSerializer

class ListWorkFlow(generics.ListAPIView):
	queryset = WorkFlow.objects.all()
	serializer_class = WorkFlowSerializer

class ListRule(generics.ListAPIView):
	queryset = Rules.objects.all()
	serializer_class = RuleSerializer	