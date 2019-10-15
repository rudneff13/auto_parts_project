from django.db import models
from django.urls import reverse


class Truck(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Truck')

    class Meta:
        verbose_name = 'Truck'
        verbose_name_plural = 'Trucks'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_products(self):
        return '; '.join([p.name for p in self.products.all()][:50])


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Product')
    description = models.CharField(max_length=250, blank=True, verbose_name='Description')
    trucks = models.ManyToManyField(Truck, through='ProductTruck', through_fields=('product', 'truck'),
                                    symmetrical=True, related_name='products',)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_trucks(self):
        return ', '.join([truck.name for truck in self.trucks.all()][:50])

    # def get_absolute_url(self):
    #     return reverse('product-detail', kwargs={'pk': self.pk})


class ProductTruck(models.Model):
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('product', 'truck')
