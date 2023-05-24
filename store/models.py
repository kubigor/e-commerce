from django.contrib.auth.models import User
from django.db import models
from django.db.models.query import QuerySet
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    address = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = ("category")
        verbose_name_plural = ("categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.address])


class ProductManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super(ProductManager, self).get_queryset().filter(is_active=True)


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="product", on_delete=models.CASCADE)
    category_by = models.ForeignKey(
        User, related_name="product_creator", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='unknown')
    image = models.ImageField(upload_to="images/", default='images/cow.jpg')
    address = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.address])
