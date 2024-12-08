from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher
from django.urls import reverse


def home(request):
    return render(request, 'index.html')


def teacher_list(request):
    teacher = Teacher.objects.all()
    ctx = {'teachers': teacher}
    return render(request, 'teachers/list.html', ctx)


def teacher_create(request):
    if request.method == 'POST':

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        subject = request.POST.get('subject')



        student = Teacher(first_name=first_name, last_name=last_name, subject=subject)
        student.save()

        return redirect('teachers:list')
    return render(request, 'teachers/form.html')


def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    delete_url = reverse('teachers:delete', args=[teacher.pk])
    return render(request, 'teachers/detail.html', {'teachers': teacher, 'delete_url': delete_url})


def teacher_edit(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)

    if request.method == 'POST':
        teacher.first_name = request.POST.get('first_name')
        teacher.last_name = request.POST.get('last_name')
        teacher.subject = request.POST.get('subject')
        teacher.save()
        return redirect('teachers:detail', pk=teacher.pk)

    return render(request, 'teachers/form.html', {'teacher': teacher})


def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)

    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher:list')

    return render(request, 'teacher/list.html', {'teacher': teacher})