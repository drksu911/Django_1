from django.views.generic import ListView, DetailView, CreateView, View
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Product, Contact
from .forms import ProductForm

class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'
    paginate_by = 4

class ContactsView(View):
    template_name = 'catalog/contacts.html'

    def get(self, request, *args, **kwargs):
        contact_info = Contact.objects.first()
        return render(request, self.template_name, {'contact_info': contact_info})

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}, Телефон: {phone}, Сообщение: {message}')
        contact_info = Contact.objects.first()
        context = {'contact_info': contact_info, 'success': True}
        return render(request, self.template_name, context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('home')