from django.db import models

# Create your models here.
class empdata(models.Model):
    name=models.CharField()
    age=models.IntegerField()
    email=models.EmailField()
    phone=models.TextField()
    department=models.TextField()
    salary=models.TextField()