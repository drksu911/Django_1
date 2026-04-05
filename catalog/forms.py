from django import forms
from .models import Product

# Список запрещённых слов (все в нижнем регистре)
FORBIDDEN_WORDS = [
    'казино', 'криптовалюта', 'крипта', 'биржа',
    'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'image']
        labels = {
            'name': 'Название',
            'description': 'Описание',
            'price': 'Цена',
            'category': 'Категория',
            'image': 'Изображение',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Стилизация всех полей формы
        for field_name, field in self.fields.items():
            # Для CheckboxInput (поле is_published не используется, но на всякий случай)
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'
        # Отдельно для поля category (выпадающий список)
        self.fields['category'].widget.attrs['class'] = 'form-select'

    def clean_name(self):
        """Валидация названия продукта на запрещённые слова."""
        name = self.cleaned_data.get('name')
        if name:
            name_lower = name.lower()
            for word in FORBIDDEN_WORDS:
                if word in name_lower:
                    raise forms.ValidationError(
                        f'Название содержит запрещённое слово "{word}".'
                    )
        return name

    def clean_description(self):
        """Валидация описания продукта на запрещённые слова."""
        description = self.cleaned_data.get('description')
        if description:
            desc_lower = description.lower()
            for word in FORBIDDEN_WORDS:
                if word in desc_lower:
                    raise forms.ValidationError(
                        f'Описание содержит запрещённое слово "{word}".'
                    )
        return description

    def clean_price(self):
        """Валидация цены: не может быть отрицательной."""
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError('Цена не может быть отрицательной.')
        return price

    def clean_image(self):
        """Валидация изображения: формат JPEG/PNG и размер не более 5 МБ."""
        image = self.cleaned_data.get('image')
        if image:
            # Проверка расширения
            ext = image.name.split('.')[-1].lower()
            if ext not in ['jpg', 'jpeg', 'png']:
                raise forms.ValidationError(
                    'Разрешены только изображения форматов JPEG и PNG.'
                )
            # Проверка размера (5 МБ = 5 * 1024 * 1024 байт)
            if image.size > 5 * 1024 * 1024:
                raise forms.ValidationError(
                    'Размер изображения не должен превышать 5 МБ.'
                )
        return image