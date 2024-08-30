from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=100)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ram = models.TextField(verbose_name='Malumotlar')  # Frame
    production_date = models.DateField(verbose_name='Ishlab chiqarilgan sana')  # Production date
    capacity = models.IntegerField(verbose_name='Odam-soni')  # Seating capacity
    image = models.ImageField(upload_to='car_images/')  # Car image


    def __str__(self):
        return f"{self.brand.name} {self.model_name} "
