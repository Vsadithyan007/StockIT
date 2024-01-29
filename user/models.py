from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    Staff=models.OneToOneField(User,on_delete=models.CASCADE)
    Address=models.CharField(max_length=220)
    Phone=models.CharField(max_length=12)
    image=models.ImageField(default='img.png',upload_to='profile_images')

    def __str__(self) -> str:
        return f'{self.Staff.username}-Profile'