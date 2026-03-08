from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # обязательно импортируем settings
from django.conf.urls.static import static  # для работы с медиафайлами

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')),
]

# Добавляем обработку медиафайлов в режиме разработки (если используете)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)