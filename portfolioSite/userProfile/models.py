from django.db import models

# Create your models here.
from django.contrib.auth.models import User
# Create your models here.

class Proposal(models.Model):
    user = models.ForeignKey(User, db_column="user",on_delete=models.CASCADE, blank=True, null=True )
    textProposal = models.TextField(max_length=10000)