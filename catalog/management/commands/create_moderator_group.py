from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product

class Command(BaseCommand):
    help = 'Создаёт группу "Модератор продуктов" и назначает права can_unpublish_product и delete_product'

    def handle(self, *args, **options):
        content_type = ContentType.objects.get_for_model(Product)

        # Право на отмену публикации (кастомное)
        can_unpublish, _ = Permission.objects.get_or_create(
            codename='can_unpublish_product',
            name='Может отменять публикацию продукта',
            content_type=content_type,
        )

        # Стандартное право на удаление продукта
        delete_perm = Permission.objects.get(
            codename='delete_product',
            content_type=content_type,
        )

        group, created = Group.objects.get_or_create(name='Модератор продуктов')
        if created:
            self.stdout.write('Группа "Модератор продуктов" создана.')
        else:
            self.stdout.write('Группа "Модератор продуктов" уже существует.')

        group.permissions.add(can_unpublish, delete_perm)
        group.save()
        self.stdout.write(self.style.SUCCESS('Права успешно назначены.'))