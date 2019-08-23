# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=30, default='')
    
    def __str__(self):
        return self.name
        
class Category(models.Model):
    type = models.CharField(max_length=30, default='')

    
    def __str__(self):
        return self.type
        
class Product(models.Model):
    name = models.CharField(max_length=30, default='')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return '{} - {} - {}'.format(self.brand, self.category, self.name)
    
