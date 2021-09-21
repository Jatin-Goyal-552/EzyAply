from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Internships(models.Model):
    iid=models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=200)
    description=models.TextField(max_length=500)
    duration= models.CharField(max_length=200,blank=True)
    cpi = models.CharField(max_length=200,blank=True)
    semester = models.CharField(max_length=100)
    other_qualifications=models.TextField(blank=True)
    stipend=models.FloatField(blank=True)
    date=models.DateTimeField(blank=True)
    def __str__(self):
        return f"{self.iid}-{self.company_name}"

class Apply(models.Model):
    a_id=models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    internship=models.ForeignKey(Internships,on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=200)
    sem=models.CharField(max_length=200)
    cpi=models.CharField(max_length=200)
    precentage_10=models.CharField(max_length=200)
    precentage_12=models.CharField(max_length=200)
    resume=models.FileField()
    def __str__(self):
        return f"{self.a_id}-{self.user}-{self.internship}"
    @property
    def imageURL(self):
        try:
            url = self.resume.url
        except:
        	url = ''
        return url