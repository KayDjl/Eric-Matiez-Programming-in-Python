from django.db import models

# Create your models here.

class Pizza(models.Model):
    
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Topping(models.Model):
    
    key = models.ForeignKey(Pizza, related_name='toppings', on_delete=models.CASCADE)
    toppings = models.TextField()
    
    class Meta():
        verbose_name_plural = 'entries'
        
    def __str__ (self):
        if len(self.toppings) > 50:
            return f"{self.toppings[:50]}..."
        else:
            return self.toppings
