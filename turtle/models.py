from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Thurtle(models.Model):
    class Meta:
        verbose_name = 'Список черепах'
        verbose_name_plural = 'Список черепах'

    name = models.CharField(max_length=200)
    color = models.CharField(max_length=7, null=True)


    def __str__(self):
        return self.name

class Cards(models.Model):
    class Meta:
        verbose_name = 'Карточки'
        verbose_name_plural = 'Карточки'
    STATUS_CHOICES = (
        (1, "Веперед"),
        (0, "Назад"),
    )
    direction = models.IntegerField(choices=STATUS_CHOICES)
    idThurtle = models.ForeignKey(Thurtle, on_delete=models.CASCADE)
    step = models.DecimalField(max_digits=2, decimal_places=0, default=1,  validators=[
            MaxValueValidator(2),
            MinValueValidator(0)
        ])



