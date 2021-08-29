from django.db import models
from django.db.models.fields import CharField


class Person(models.Model):
    CATEGORY = (
        ('Indoor','Outdoor'),('Out door', 'IN door')
    )
    Firstname=models.CharField(max_length=20)
    Lastname=models.CharField(max_length=20)
    category=models.CharField(max_length=255,null=True,choices=CATEGORY)
    Email=CharField(max_length=100)
    PhoneNo=models.IntegerField()
