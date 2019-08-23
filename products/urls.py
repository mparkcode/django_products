from django.conf.urls import url
from .views import all_products, all_brands, all_categories, get_products_by_brand, get_products_by_category

urlpatterns = [
    url(r'all_products/$', all_products, name='all_products'),
    url(r'all_brands/$', all_brands, name='all_brands'),
    url(r'all_categories/$', all_categories, name='all_categories'),
    url(r'products_by_brands/(?P<brand>[-\w]+)$', get_products_by_brand, name='get_products_by_brand'),
    url(r'products_by_category/(?P<category>[-\w]+)$', get_products_by_category, name='get_products_by_category'),
]