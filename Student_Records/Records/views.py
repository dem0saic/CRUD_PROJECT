from django.shortcuts import render
from .models import Student
from.forms import StudentForm
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, 'index.html', {
        'students': Student.objects.all(),
    })

def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def get_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student_id = form.cleaned_data['student_id']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_student_age = form.cleaned_data['student_age']
            new_email = form.cleaned_data['email']
            new_phone_number = form.cleaned_data['phone_number']
            new_location = form.cleaned_data['location']
            new_hobby = form.cleaned_data['hobby']

            new_student = Student(
                student_id = new_student_id, 
                first_name = new_first_name, 
                last_name = new_last_name, 
                student_age = new_student_age, 
                email = new_email, 
                phone_number = new_phone_number, 
                location = new_location, 
                hobby = new_hobby
            )
            new_student.save()
        form.save()
        return render(request, 'students/get_student.html', {
            'form': StudentForm(),
            'success': True, 
        })
    else:
        form = StudentForm()
    return render(request, 'get_student.html', {
        'form': form,
    })