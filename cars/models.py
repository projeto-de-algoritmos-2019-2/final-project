from django.db import models

class Car(models.Model):
    
    year = models.IntegerField()
    model = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    image = models.ImageField(upload_to='car_images', default='default.jpg')

    def __str__(self):
        return f'{self.model} {self.manufacturer} {self.year}'