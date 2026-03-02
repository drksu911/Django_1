import os
import json
import django

# Настройка Django (должна быть ПЕРЕД импортом моделей)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

# Теперь можно импортировать модели
from django.core import serializers
from catalog.models import Category, Product

# Создаём папку fixtures, если её нет
os.makedirs('catalog/fixtures', exist_ok=True)

# Сохраняем категории
with open('catalog/fixtures/categories.json', 'w', encoding='utf-8') as f:
    data = serializers.serialize('json', Category.objects.all(), indent=4)
    f.write(data)

# Сохраняем продукты
with open('catalog/fixtures/products.json', 'w', encoding='utf-8') as f:
    data = serializers.serialize('json', Product.objects.all(), indent=4)
    f.write(data)

print("Фикстуры успешно созданы в UTF-8 без BOM")