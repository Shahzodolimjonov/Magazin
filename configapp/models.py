from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Role(models.Model):
    name = models.CharField(max_length=100)


class CustomUser(AbstractUser):
    roles = models.ManyToManyField(Role)


class Category(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def str(self):
        return self.title


class Shop(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField()

    def str(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    publish_date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    image = models.URLField()
    main_image = models.URLField()
    orders = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    categories = models.ManyToManyField('Category', related_name='products')

    def str(self):
        return self.title
