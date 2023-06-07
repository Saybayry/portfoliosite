from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ElPortfolio(models.Model):
    user = models.ForeignKey(User, db_column="user",on_delete=models.CASCADE, blank=True, null=True )
    img = models.ImageField(upload_to='users/', blank=True, null=True)
