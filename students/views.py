from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.urls import reverse
from django.contrib import messages


def home(request):
    return render(request, 'index.html')


def student_list(request):
    students = Student.objects.all()
    ctx = {'students': students}
    return render(request, 'students/list.html', ctx)


def student_create(request):
    if request.method == 'POST':

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        email = request.POST.get('email')

        if Student.objects.filter(email=email).exists():
            messages.error(request, "Bu email manzili allaqachon ro'yxatdan o'tgan.")
            return redirect('students:create')

        student = Student(first_name=first_name, last_name=last_name, age=age, email=email)
        student.save()

        #
        return redirect('students:list')
    return render(request, 'students/form.html')


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    delete_url = reverse('students:delete', args=[student.pk])
    return render(request, 'students/detail.html', {'student': student, 'delete_url': delete_url})


def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.first_name = request.POST.get('first_name')
        student.last_name = request.POST.get('last_name')
        student.age = request.POST.get('age')
        student.email = request.POST.get('email')
        student.save()
        return redirect('students:detail', pk=student.pk)

    return render(request, 'students/form.html', {'student': student})


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.delete()
        return redirect('students:list')

    return render(request, 'students/list.html', {'student': student})