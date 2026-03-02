import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from django.core import serializers
from catalog.models import Category, Product

with open('catalog/fixtures/categories.json', 'w', encoding='utf-8') as f:
    f.write(serializers.serialize('json', Category.objects.all(), indent=4))
with open('catalog/fixtures/products.json', 'w', encoding='utf-8') as f:
    f.write(serializers.serialize('json', Product.objects.all(), indent=4))
print("Фикстуры созданы")