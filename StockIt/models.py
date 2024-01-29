from django.db import models
from django.contrib.auth.models import User

CATEGORY=(
    ('Laptops','Laptops'),
    ('Desktop Computers','Desktop Computers'),
    ('CPU','CPU'),
    ('Projectors','Projectors'),
    ('Printers','Printers'),
    ('Cables and Adapters','Cables and Adapters'),
)

class Product(models.Model):
    Name = models.CharField(max_length=100)
    Category = models.TextField(max_length=100,choices=CATEGORY)
    Quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural='Staff Product'

    def __str__(self):
        return f'{self.Name}-{self.Quantity}'
    
    
class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    staff=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    o_qty=models.PositiveIntegerField(null=True)
    date=models.DateTimeField(auto_now_add=True)

    
    class Meta:
        verbose_name_plural='Order'

    def __str__(self):
        return f'{self.product} Ordered by {self.staff.username}'
