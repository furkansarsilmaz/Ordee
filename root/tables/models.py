from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.price} $"
    
class Order(models.Model):
    menu_item = models.ForeignKey(Menu,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.menu_item.name} - {self.quantity}"