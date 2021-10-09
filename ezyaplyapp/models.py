from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Internships(models.Model):
    iid=models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=200)
    intern_role=models.CharField(max_length=200,blank=True)
    description=models.TextField(max_length=500,null=True)
    duration= models.CharField(max_length=200,blank=True,null=True)
    cpi = models.CharField(max_length=200,blank=True,null=True)
    semester = models.CharField(max_length=100,null=True)
    other_qualifications=models.TextField(blank=True,null=True)
    stipend=models.FloatField(blank=True,null=True)
    date=models.CharField(max_length=100,null=True)
    def __str__(self):
        return f"{self.iid}"

class Apply(models.Model):
    a_id=models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    internship=models.ForeignKey(Internships,on_delete=models.CASCADE,null=True)
    user_name=models.CharField(max_length=500,null=True)
    user_email=models.EmailField(null=True, blank=True)
    phone_number=models.CharField(max_length=200,null=True)
    sem=models.CharField(max_length=200,null=True)
    cpi=models.CharField(max_length=200,null=True)
    precentage_10=models.CharField(max_length=200,null=True)
    precentage_12=models.CharField(max_length=200,null=True)
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

class Announcement(models.Model):
    an_id=models.AutoField(primary_key=True)
    announcement_date=models.CharField(max_length=200,null=True)
    announcement_text=models.TextField(max_length=1000, null=True)

class Profile(models.Model):
    p_id=models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    user_name=models.CharField(max_length=500,null=True)
    user_email=models.EmailField(null=True, blank=True)
    phone_number=models.CharField(max_length=200,null=True)
    sem=models.CharField(max_length=200,null=True)
    cpi=models.CharField(max_length=200,null=True)
    precentage_10=models.CharField(max_length=200,null=True)
    precentage_12=models.CharField(max_length=200,null=True)
    resume=models.FileField(null=True)