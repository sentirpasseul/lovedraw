from django.db import models

class Picture(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    artist = models.ForeignKey('Artist', null=True, on_delete=models.PROTECT, verbose_name='Художник')
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

class Artist(models.Model):
    artist = models.CharField(max_length=20, db_index=True, verbose_name='Художник')

    def __str__(self):
        return self.artist

    class Meta:
        verbose_name_plural = 'Художники'
        verbose_name = 'Художник'
        ordering = ['artist']