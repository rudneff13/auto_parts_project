from django.db import models


class Truck(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Автомобиль')

    def get_products(self):
        return '; '.join([p.name for p in self.products.all()])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Truck'
        verbose_name_plural = 'Trucks'
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Изделие')
    description = models.CharField(max_length=250, null=True, blank=True, verbose_name='Описание')
    trucks = models.ManyToManyField(Truck, through='ProductTruck', through_fields=('product', 'truck'),
                                    symmetrical=True, related_name='products')

    def __str__(self):
        return self.name

    def get_trucks(self):
        return ', '.join([truck.name for truck in self.trucks.all()])

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']


class ProductTruck(models.Model):
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('product', 'truck')
