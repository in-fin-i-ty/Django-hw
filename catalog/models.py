from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='название товара')
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='название товара')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(upload_to="imagines/",  verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категории')
    price = models.IntegerField(verbose_name='цена')
    date_create = models.DateField(verbose_name='дата создания', auto_now_add=True, **NULLABLE)
    last_modified_date = models.DateField(verbose_name='дата последнего изменения', auto_now=True, **NULLABLE)

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.description}"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='название блога')
    slug = models.CharField(verbose_name='Альт.название', max_length=255, unique=True, **NULLABLE)
    body = models.TextField(verbose_name='контент', **NULLABLE)
    preview = models.ImageField(upload_to="imagines/", verbose_name='изображение', **NULLABLE)
    date_create = models.DateField(verbose_name='дата создания', auto_now_add=True)
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блог'
