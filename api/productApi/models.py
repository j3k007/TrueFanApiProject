from django.db import models

# Create your models here.

class Products(models.Model):
    product_id: int = models.AutoField(primary_key=True)
    name: str = models.CharField(max_length=250)
    category: str = models.CharField(max_length=250, choices=(
        ("Frozen Food", "Forzen Food"), 
        ("Vegi","Vegi"),
        ("Non-Veg","Non-Veg"), 
        ("Bevrages","Bevrages")))
    price: float = models.FloatField(max_length=250, default=None)

    def __str__(self):
        return self.name
