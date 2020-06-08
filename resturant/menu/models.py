from django.db import models


# Create your models here.


class Dish(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Dishes'
