from django.db import models

class Category(models.Model):
    code = models.CharField(max_length=30, verbose_name='Mã', unique=True)
    name = models.CharField(max_length=200, verbose_name='Tên')
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField(upload_to='static/images')
    def __str__(self):
        return self.name

