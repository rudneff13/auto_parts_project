from rest_framework import serializers

from .models import Truck, Product, ProductTruck


class ProductTruckSerializer(serializers.ModelSerializer):
    # truck = serializers.ReadOnlyField(source='truck.name')
    # name = serializers.CharField(source='truck.name')
    name = serializers.CharField(source='truck.name',)
    # truck_pk = serializers.ReadOnlyField(source='truck.pk')
    # product = serializers.ReadOnlyField(source='product.name')
    # product.pk = serializers.ReadOnlyField(source='product.pk')

    class Meta:
        model = ProductTruck
        fields = ('name',)


class TruckSerializer(serializers.ModelSerializer):

    class Meta:
        model = Truck
        fields = ('pk', 'name', 'products')
        depth = 1


class ProductSerializer(serializers.ModelSerializer):
    trucks = ProductTruckSerializer(source='producttruck_set', many=True,)

    class Meta:
        model = Product
        fields = ('pk', 'name', 'description', 'trucks')
        # depth = 1

    def create(self, validated_data):
        trucks_data = validated_data.pop('producttruck_set')
        prod = Product.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
        )
        for obj in trucks_data:
            tr = Truck.objects.get_or_create(**obj['truck'])
            ProductTruck(product=prod, truck=tr[0]).save()
        return prod

    def update(self, instance, validated_data):
        trucks_data = validated_data.pop('producttruck_set')
        instance.trucks.clear()
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        for obj in trucks_data:
            tr = Truck.objects.get_or_create(**obj['truck'])
            ProductTruck(product=instance, truck=tr[0]).save()
        return instance
