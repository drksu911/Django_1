from django.shortcuts import render, get_object_or_404
from .models import Product, Contact
from .forms import ProductForm  # если вы создавали форму для добавления товара
from django.shortcuts import redirect

def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/home.html', context)

def contacts(request):
    # Получаем первый контакт из базы (или None, если записей нет)
    contact_info = Contact.objects.first()
    context = {'contact_info': contact_info}
    if request.method == 'POST':
        # Обработка данных формы обратной связи
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}, Телефон: {phone}, Сообщение: {message}')
        context['success'] = True  # флаг успешной отправки
    return render(request, 'catalog/contacts.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'catalog/product_detail.html', context)

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'catalog/product_form.html', {'form': form})