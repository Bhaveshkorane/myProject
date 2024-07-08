from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class empdata(models.Model):
    name=models.CharField()
    age=models.IntegerField()
    email=models.EmailField()
    phone=models.TextField()
    department=models.TextField()
    salary=models.TextField()


User=get_user_model()

# class profile(models.Model):
#     username=models.ForeignKey(User,on_delete=models.CASCADE)
#     first_name=models.TextField()
#     last_name=models.TextField()
#     email=models.EmailField()
#     age=models.IntegerField()
#     gender=models.CharField()
#     location=models.TextField(blank=True)

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    location = models.CharField(max_length=100, blank=True)



    def __str__(self):
        return self.user.username

