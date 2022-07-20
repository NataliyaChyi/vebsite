from django.db import models

class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

# Create your models here.
