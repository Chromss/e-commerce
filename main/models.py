import uuid
from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=150)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def average_price(self):
        variations = self.variation_set.all()
        if variations.exists():
            total_price = sum(var.price for var in variations)
            return total_price / variations.count()
        return 0

    def variation_count(self):
        return self.variation_set.count()

    def __str__(self):
        return self.name

class Variation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, related_name='variations', on_delete=models.CASCADE)
    variation_type = models.CharField(max_length=100)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.variation_type}: IDR {self.price:,}"