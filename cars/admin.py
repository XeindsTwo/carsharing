from django.contrib import admin
from .models import Car, CarCategory, CarCharacteristics

class CarCharacteristicsInline(admin.TabularInline):
    model = CarCharacteristics
    extra = 1

class CarAdmin(admin.ModelAdmin):
    inlines = [CarCharacteristicsInline]

admin.site.register(Car, CarAdmin)
admin.site.register(CarCategory)

