from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
class myBooks(models.Model):
    title=models.CharField(max_length=64)
    author=models.CharField(max_length=64)
    genre=models.CharField(max_length=64)
    image = models.ImageField(upload_to='media/', null="Nothing")
    price=models.DecimalField(max_digits=5, decimal_places=2)
    stock=models.IntegerField(default=0)

    def get_total_price(self):
        return self.price * self.stock

    def clean(self):
        if self.price<0:
            raise ValidationError('Price can not be negative')
        if self.stock<0:
            raise ValidationError('Stock can not be negative')

    def __str__(self):
        return f" {self.id}, title:{self.title}, author: {self.author}, genre:{self.genre},picture: {self.image}, price:{self.price}, stock:{self.stock}"