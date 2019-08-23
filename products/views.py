# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Product, Brand, Category

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def all_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products, 'title': 'Shop All Products'})
    
def all_brands(request):
    brands = Brand.objects.all()
    return render(request, 'brands.html', {'brands': brands})
    
def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def get_products_by_brand(request, brand):
    brand_we_are_retrieving = get_object_or_404(Brand, name=brand)
    products = Product.objects.filter(brand=brand_we_are_retrieving)
    return render(request, 'products.html', {'products': products, 'title': '{} gear'.format(brand_we_are_retrieving.name)})
    
def get_products_by_category(request, category):
    category_we_are_retrieving = get_object_or_404(Category, type=category)
    products = Product.objects.filter(category = category_we_are_retrieving)
    return render(request, 'products.html', {'products': products, 'title': 'Browse all {}'.format(category_we_are_retrieving.type)})