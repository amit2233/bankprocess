# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.






class WorkFlow(models.Model):
    name = models.CharField(max_length=40)
    condition = models.CharField(max_length=5)
    def __str__(self):
        return self.name


class Rules(models.Model):
    Operator_C = ( ("<","Less than"), 
                   (">", "Greater than"),
                   ("<>","Not equals"),
                   ("equals","Equal")
                     )
    name = models.CharField(max_length=50)
    operator = models.CharField(max_length = 20, choices= Operator_C)
    value = models.CharField(max_length = 60)
    workflow = models.ForeignKey(WorkFlow, related_name='rule', on_delete=models.CASCADE)
    def __str__(self):
        return self.name + self.operator + self.value   


class Process(models.Model):
    name = models.CharField(max_length=40)
    origin_node = models.CharField(max_length=40)
    destination_node = models.CharField(max_length=40)
    workflow = models.ForeignKey(WorkFlow, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name    