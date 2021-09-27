from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email', 'password1', 'password2']

class ApplyForm(forms.ModelForm):
    # phone_number=forms.CharField(max_length=200,widget=forms.TextInput(attrs={"class":"form-control"}),label="Phone Number")
    # sem=forms.CharField(max_length=200,widget=forms.TextInput(attrs={"class":"form-control"}),label="Semester")
    # cpi=forms.CharField(max_length=200,widget=forms.TextInput(attrs={"class":"form-control"}),label="CPI")
    # precentage_10=forms.CharField(max_length=200,widget=forms.TextInput(attrs={"class":"form-control"}),label="10th Precentage")
    # precentage_12=forms.CharField(max_length=200,widget=forms.TextInput(attrs={"class":"form-control"}),label="12th Precentage") 
    # resume=forms.FileField(widget=forms.FileInput(attrs={"class":"form-control"}),label="Resume")
    class Meta:
        model=Apply
        fields=['user','internship','phone_number','sem','cpi','precentage_10','precentage_12','resume']
        # excluding=['user','internship']

class AddInternshipForm(forms.ModelForm):
    class Meta:
        model=Internships
        fields=['company_name','description','duration','cpi','semester','other_qualifications','stipend','date']

class MadeAnnouncementForm(forms.ModelForm):
    class Meta:
        model=Announcement
        fields=['announcement_date','announcement_text']

