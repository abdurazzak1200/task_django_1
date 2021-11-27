from django.db import models

# Create your models here.

class Images(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to='imagesy/')

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'
    def __str__(self):
        return self.name
