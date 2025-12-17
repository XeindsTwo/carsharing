from django.conf import settings
from django.db import models
from cars.models import Car


# Create your models here.
class Booking(models.Model):
    class Meta:
        verbose_name = "бронирования авто"  # как отображается для одного объекта (в Django админке)
        verbose_name_plural = "Бронирования авто"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="bookings"
    )
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    # делаем список кортежей
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('confirmed', 'Подтверждена'),
        ('cancelled', 'Отменена'),
    ]
    # используем аргумент choices, который представляет собой кортеж кортежей
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="new")
    # в момент создания записи будет генерироваться автоматически дата
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.car.name} ({self.status})"