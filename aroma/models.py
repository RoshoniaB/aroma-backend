from django.db import models
import uuid

class Wine(models.Model):
    brand_name = models.CharField(max_length=100)
    type_name = models.CharField(max_length=100)
    wine_type= models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image_url = models.CharField(max_length=10000)
    description = models.CharField(max_length=10000)
    price = models.CharField(max_length=100)
    sku = models.UUIDField(unique=True, auto_created=True, default=uuid.uuid4, editable=False)
    wine_year = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.brand_name}, {self.type_name}, {self.location}, {self.image_url}, {self.description}, {self.price}, {self.wine_year}'
