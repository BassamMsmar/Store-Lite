from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.name

class ProdctImage(models.Model):
    product = models.ForeignKey(Product, related_name='prodcut_image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')

