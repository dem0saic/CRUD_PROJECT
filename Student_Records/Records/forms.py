from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'first_name', 'last_name', 'student_age', 'email', 'phone_number', 'location', 'hobby']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'location': 'Location',
            'hobby': 'Hobby',
            'student_age': 'Age',
            'student_id': 'Student ID',
        }
        widgets = {
            'student_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}), 
            'student_age': forms.NumberInput(attrs={'class': 'form-control'}), 
            'email': forms.TextInput(attrs={'class': 'form-control'}), 
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}), 
            'location': forms.TextInput(attrs={'class': 'form-control'}), 
            'hobby': forms.TextInput(attrs={'class': 'form-control'}),
        }