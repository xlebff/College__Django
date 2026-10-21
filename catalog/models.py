from django.db import models

class Category(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)
    slug = models.SlugField('Слаг', max_length=50, unique=True)
    description = models.TextField('Описание', blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class Feature(models.Model):
    name = models.CharField('Название', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Особенность'
        verbose_name_plural = 'Особенности'
        ordering = ['name']

    def __str__(self):
        return self.name


class Zone(models.Model):
    title = models.CharField('Название зоны', max_length=100)
    subtitle = models.CharField('Подзаголовок', max_length=200, blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='zones',
        verbose_name='Категория'
    )
    price = models.DecimalField('Цена (руб/час)', max_digits=8, decimal_places=2)
    emoji = models.CharField('Эмодзи', max_length=10, blank=True)
    tag = models.CharField('Тег', max_length=30, blank=True, null=True)
    popular = models.BooleanField('Популярная', default=False)
    cpu = models.CharField('Процессор', max_length=100, blank=True)
    gpu = models.CharField('Видеокарта', max_length=100, blank=True)
    ram = models.CharField('Оперативная память', max_length=100, blank=True)
    monitor = models.CharField('Монитор', max_length=100, blank=True)
    features = models.ManyToManyField(
        Feature,
        blank=True,
        related_name='zones',
        verbose_name='Особенности'
    )
    description = models.TextField('Описание', blank=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    is_active = models.BooleanField('Активна', default=True)
    
    class Meta:
        verbose_name = 'Игровая зона'
        verbose_name_plural = 'Игровые зоны'
        ordering = ['title']

    def __str__(self):
        return self.title