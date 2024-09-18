import uuid
from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=400)
    image = models.ImageField(upload_to='', blank=True, null=True)
    variation_count = models.IntegerField(default=0)
    minimum_price = models.IntegerField(default=0)