from django.db import models

# Create your models here.

class Companies(models.Model):
    org=models.CharField(max_length=100)
    date=models.DateField(auto_now=False, auto_now_add=False)
    required=models.IntegerField()
    role=models.CharField(max_length=50)
    package=models.FloatField()
    taken=models.IntegerField()
    whom=models.TextField()
    class Meta:
        db_table='companies'

class Candidates(models.Model):
    regno=models.IntegerField()
    gender=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    dept=models.CharField(max_length=50)
    batch=models.IntegerField()
    contact=models.IntegerField()
    email=models.EmailField(max_length=254)
    address=models.CharField(max_length=50)
    cgpa=models.IntegerField()
    hsc=models.IntegerField()
    diploma=models.IntegerField()
    sslc=models.IntegerField()
    career=models.CharField(max_length=50)
    skills=models.CharField(max_length=50)
    placed=models.CharField(max_length=50)
    status=models.CharField(max_length=50)

    def __str__(self):
        return self.name+" is affected"

    class Meta:
        db_table='candidates'
