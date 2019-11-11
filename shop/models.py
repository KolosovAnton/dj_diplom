from django.db import models
from django.utils.text import slugify


# пункты меню
class Catalog(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=50)
    short_name = models.CharField(max_length=15, unique=True)

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'

    def __str__(self):
        return '{}'.format(self.title)


# подпункты меню
class Categories(models.Model):
    title = models.CharField(max_length=50)
    short_name = models.CharField(max_length=15, unique=True)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return '{}'.format(self.title)


# товары
class Product(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='static')
    body = models.TextField()
    short_name = models.CharField(max_length=15, unique=True)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return '{}'.format(self.name)


# статьи
class Article(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    published_at = models.DateTimeField()
    product = models.ManyToManyField(Product, related_name='articles')
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-published_at']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return '{}'.format(self.title)


# отзывы
class Review(models.Model):
    name = models.TextField()
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return str(self.product.name) + ' ' + self.text[:50]
