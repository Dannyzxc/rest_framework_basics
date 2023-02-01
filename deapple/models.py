from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50, default="")
    stu_id = models.IntegerField(default="")
    place = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name
