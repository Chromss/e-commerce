from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-inventory/', show_add_inventory, name='show_add_inventory'),
    path('product/', show_product, name='show_product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)