from django.db import models


# продолжать код можно в том же файле спокойно
class CarCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "категория авто"  # как отображается для одного объекта (в Django админке)
        verbose_name_plural = "Категории авто"  # как отображается для списка (в Django админке)

    def __str__(self):
        return f"{self.name}"


class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    color = models.CharField(max_length=100)
    year = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField(
        upload_to='cars/',
        blank=False,
        null=True)
    is_available = models.BooleanField(default=True)

    category = models.ForeignKey(
        CarCategory,
        on_delete=models.CASCADE,
        related_name='cars',
        null=True,  # чтобы по умолчанию было значение null
    )

    class Meta:
        verbose_name = "авто"
        verbose_name_plural = "Автомобили"
        ordering = ['-price']

    def __str__(self):
        return f"{self.name} ({self.year}) - {self.price}"


class CarCharacteristics(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name="characteristics"
    )

    class Meta:
        verbose_name = "Характеристики авто"
        verbose_name_plural = "Характеристики авто"

    def __str__(self):
        return f"{self.name}: {self.value}"
