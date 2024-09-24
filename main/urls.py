from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-inventory/', show_add_inventory, name='show_add_inventory'),
    path('product/', show_product, name='show_product'),
    path('signup/', show_signup, name='show_signup'),
    path('login/', show_login, name='show_login'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)