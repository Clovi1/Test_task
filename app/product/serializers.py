from rest_framework import serializers

from .models import ProductImages, Product


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    images = ProductImagesSerializer(many=True, read_only=True)
    time_create = serializers.DateTimeField(format='%H:%M %d.%m.%Y', read_only=True)
    uploaded_images = serializers.ListField(child=serializers.ImageField(), write_only=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'owner', 'time_create', 'images', 'uploaded_images',)

    def create(self, validated_data):
        uploaded_data = validated_data.pop('uploaded_images')
        new_product = Product.objects.create(**validated_data)
        for uploaded_item in uploaded_data:
            ProductImages.objects.create(product=new_product, image=uploaded_item)
        return new_product

    def update(self, instance, validated_data):
        uploaded_data = validated_data.get('uploaded_images')
        if uploaded_data:
            instance.images.clear()
            for uploaded_item in uploaded_data:
                ProductImages.objects.create(product=instance, image=uploaded_item)

        return super().update(instance, validated_data)
