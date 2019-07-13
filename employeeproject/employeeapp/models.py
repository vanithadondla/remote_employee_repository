from django.db import models
class employeedata(models.Model):
    name1=models.CharField(max_length=100)
    location1=models.CharField(max_length=100)
    email1=models.EmailField(max_length=100)
    mobile1=models.BigIntegerField()
    username1=models.CharField(max_length=100)
    password1=models.CharField(max_length=100)


