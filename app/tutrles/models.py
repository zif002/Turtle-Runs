from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Turtle(models.Model):
    class Meta:
        verbose_name = u'Черепаха'
        verbose_name_plural = u'Черепахи'
    COLORS = (
        ('white', 'Белая'),
        ('blue', 'Синяя'),
        ('violet', 'Фиолетовая'),
        ('yellow', 'Желтая'),
        ('red', 'Красная'),
        ('green', 'Зеленая'),
    )
    id_thurtle = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name="Имя черепахи")
    color = models.CharField(max_length=10, choices=COLORS, verbose_name="Цвет")


    def __str__(self):
        return self.name

class Cards(models.Model):
    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'
    COLORS = (
        (1, 'Любая'),
        (2, 'Синяя'),
        (3, 'Фиолетовая'),
        (4, 'Желтая'),
        (5, 'Красная'),
        (6, 'Зеленая'),
        (7, 'Последняя'),
    )
    DIRACTION = (
        (0, 'Назад'),
        (1, 'Вперед'),
    )
    COUNTSTEP = (
        (1, '1'),
        (2, '2'),
    )
    cards_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name="Название")
    color = models.IntegerField(choices=COLORS,  default=1, verbose_name="Цвет")
    diraction = models.IntegerField(choices=DIRACTION,  default=0, verbose_name="Направление")
    count_step = models.IntegerField(choices=COUNTSTEP,  default=1, verbose_name="Количество шагов")

    def __str__(self):
        return self.name
 
