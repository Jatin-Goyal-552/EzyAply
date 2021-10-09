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
    class Meta:
        model=Apply
        fields=['user','internship','user_name','user_email','phone_number','sem','cpi','precentage_10','precentage_12','resume']

class AddInternshipForm(forms.ModelForm):
    class Meta:
        model=Internships
        fields=['company_name','intern_role','description','duration','cpi','semester','other_qualifications','stipend','date']

class MadeAnnouncementForm(forms.ModelForm):
    class Meta:
        model=Announcement
        fields=['announcement_date','announcement_text']

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['user','user_name','user_email','phone_number','sem','cpi','precentage_10','precentage_12','resume']

