from dataclasses import fields
from tkinter import Widget
from django import forms
from .models import Resume

GENDER_CHOICES=[('Male','Male'),('Female','Female')]
CITY_CHOICES=[('Cochin','Cochin'),("Chennai","Chennai"),("Banglore","Banglore"),('Mysore','Mysore'),('Delhi','Delhi'),('Hyderabad','Hyderabad')]
class DateInput(forms.DateTimeInput):
    input_type="date"
class ResumeForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    job_city=forms.MultipleChoiceField(choices=CITY_CHOICES,label="Prefered Job Location",widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=Resume
        fields=['name','dob','gender','locality','city','pin','state','mobile','email','job_city','profile_img','file_doc']
        labels={'name':'Full Name','dob':'Date of Birth','pin':'Pin Code','mobile':'Mobile No','profile_img':'Profile Image','file_doc':'Resume','email':'Email ID'}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'dob':DateInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-select'}),
        }
        


        