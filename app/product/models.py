from django.db import models


class Product(models.Model):
    title = models.CharField('Название', max_length=255)
    price = models.PositiveIntegerField('Цена')
    owner = models.ForeignKey('auth.User', verbose_name='Автор', related_name='product', on_delete=models.CASCADE)
    time_create = models.DateTimeField("Время создания", auto_now_add=True)

    def __str__(self):
        return self.title


class ProductImages(models.Model):
    product = models.ForeignKey(Product, verbose_name='Товар', related_name='images', on_delete=models.CASCADE,
                                null=True)
    image = models.ImageField('Изображение', upload_to='images')
