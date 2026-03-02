from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Заполняет базу тестовыми продуктами (удаляет существующие)'

    def handle(self, *args, **options):
        # Удаляем все существующие продукты и категории
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write('Старые данные удалены.')

        # Создаём категории
        electronics = Category.objects.create(name="Электроника", description="Гаджеты")
        clothes = Category.objects.create(name="Одежда", description="Мода")
        books = Category.objects.create(name="Книги", description="Литература")

        # Создаём продукты
        products_data = [
            {"name": "Смартфон", "description": "Новый смартфон", "price": 500, "category": electronics},
            {"name": "Ноутбук", "description": "Игровой ноутбук", "price": 1200, "category": electronics},
            {"name": "Футболка", "description": "Хлопок", "price": 20, "category": clothes},
            {"name": "Джинсы", "description": "Синие джинсы", "price": 45, "category": clothes},
            {"name": "Питон", "description": "Книга по Python", "price": 30, "category": books},
        ]
        for item in products_data:
            Product.objects.create(
                name=item["name"],
                description=item["description"],
                price=item["price"],
                category=item["category"]
            )
        self.stdout.write(self.style.SUCCESS('Тестовые продукты успешно добавлены.'))