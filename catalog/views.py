from django.shortcuts import render
from .models import Contact, Product


def home(request):
    """Главная страница"""
    latest_products = Product.objects.order_by('-created_at')[:5]
    print(latest_products)  # в консоль
    return render(request, 'catalog/home.html')


def contacts(request):
    """Страница контактов с обработкой формы"""
    success_message = None
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Здесь можно сохранить данные в базу или отправить письмо
        # Для демонстрации просто покажем сообщение
        success_message = f"Спасибо, {name}! Ваше сообщение отправлено."
        # Можно также вывести в консоль
        print(f"Получено сообщение от {name} ({email}): {message}")

    return render(request, 'catalog/contacts.html', {'success_message': success_message})