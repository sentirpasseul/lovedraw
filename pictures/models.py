from django.db import models

class Picture(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    content = models.TextField(max_length=50, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')

    style = models.ForeignKey('Style', null=True, on_delete=models.PROTECT, verbose_name='Стиль')


    class Meta:
        verbose_name_plural = 'Картины'
        verbose_name = 'Картина'
        ordering = ['-published']
# Create your models here.

class Style(models.Model):

    style = models.CharField(max_length=20, db_index=True, verbose_name="Стиль")

    def __str__(self):
        return self.style

    class Meta:
        verbose_name_plural = 'Стили'
        verbose_name = 'Стиль'
        ordering = ['style']

