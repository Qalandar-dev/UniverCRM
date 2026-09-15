from django.db.models import Q, Count
from django.shortcuts import render,redirect
from.models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from . import service
import json
# Create your views here.

def login_required_decorator(func):
    return login_required(func, login_url='login_page')

@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect('login_page')

def login_page(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect('home_page')
    return render(request, 'login.html')

@login_required_decorator
def home_page(request):
    faculties = service.get_faculties()
    kafedras = service.get_kafedra()
    subjects = service.get_subject()
    teachers = service.get_teacher()
    groups = service.get_group()
    students = service.get_student()

    ctx = {
        'counts':{
            'faculties':len(faculties),
            'kafedras':len(kafedras),
            'subjects':len(subjects),
            'teachers':len(teachers),
            'groups':len(groups),
            'students':len(students),
        }
    }
    return render(request,'index.html',ctx)

@login_required_decorator
def faculty_create(request):
    model = Faculty()
    form = FacultyForm(request.POST or None,instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('faculty_list')
    ctx = {
        'form':form
    }
    return render(request,'faculty/form.html',ctx)

@login_required_decorator
def faculty_edit(request,pk):
    model = Faculty.objects.get(pk=pk)
    form = FacultyForm(request.POST or None,instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('faculty_list')
    ctx = {
        'form':form,
        'model':model
    }
    return render(request,'faculty/form.html',ctx)

@login_required_decorator
def faculty_delete(request,pk):
    model = Faculty.objects.get(pk=pk)
    model.delete()
    return redirect('faculty_list')

@login_required_decorator
def faculty_list(request):
    faculties = service.get_faculties()
    print(faculties)
    ctx = {
        'faculties':faculties
    }
    return render(request,'faculty/list.html',ctx)

@login_required_decorator
def kafedra_create(request):
    model = Kafedra()
    form = KafedraForm(request.POST or None,instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('kafedra_list')
    ctx = {
        'form':form
    }
    return render(request,'kafedra/form.html',ctx)

@login_required_decorator
def kafedra_edit(request,pk):
    model = Kafedra.objects.get(pk=pk)
    form = KafedraForm(request.POST or None,instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('kafedra_list')
    ctx = {
        'form':form,
        'model':model
    }
    return render(request,'kafedra/form.html',ctx)

@login_required_decorator
def kafedra_delete(request,pk):
    model = Kafedra.objects.get(pk=pk)
    model.delete()
    return redirect('kafedra_list')

@login_required_decorator
def kafedra_list(request):
    kafedras = service.get_kafedra()
    ctx = {
        'kafedras':kafedras
    }
    return render(request,'kafedra/list.html',ctx)

@login_required_decorator
def subject_create(request):
    model = Subject()
    form = SubjectForm(request.POST or None,instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('subject_list')
    ctx = {
        'form':form
    }
    return render(request,'subject/form.html',ctx)

@login_required_decorator
def subject_edit(request,pk):
    model = Subject.objects.get(pk=pk)
    form = SubjectForm(request.POST or None,instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('subject_list')
    ctx = {
        'model':model,
        'form':form
    }
    return render(request,'subject/form.html',ctx)

@login_required_decorator
def subject_delete(request,pk):
    model = Subject.objects.get(pk=pk)
    model.delete()
    return redirect('subject_list')

@login_required_decorator
def subject_list(request):
    subjects = service.get_subject()
    ctx = {
        'subjects':subjects
    }
    return render(request,'subject/list.html',ctx)

@login_required_decorator
def teacher_create(request):
    model = Teacher()
    form = TeacherForm(request.POST or None,instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('teacher_list')
    ctx = {
        'form':form
    }
    return render(request,'teachers/form.html',ctx)

@login_required_decorator
def teacher_edit(request,pk):
    model = Teacher.objects.get(pk=pk)
    form = TeacherForm(request.POST or None,instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('teacher_list')
    ctx = {
        'model':model,
        'form':form
    }
    return render(request,'teachers/form.html',ctx)

@login_required_decorator
def teacher_delete(request,pk):
    model = Teacher.objects.get(pk=pk)
    model.delete()
    return redirect('teacher_list')

@login_required_decorator
def teacher_list(request):
    teachers = service.get_teacher()
    ctx = {
        'teachers':teachers
    }
    return render(request,'teachers/list.html',ctx)

@login_required_decorator
def group_create(request):
    model = Group()
    form = GroupForm(request.POST or None,instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('group_list')
    ctx = {
        'form':form
    }
    return render(request , 'groups/form.html',ctx)

@login_required_decorator
def group_edit(request,pk):
    model = Group.objects.get(pk=pk)
    form = GroupForm(request.POST or None,instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('group_list')
    ctx = {
        'model':model,
        'form':form
    }
    return render(request,'groups/form.html',ctx)

@login_required_decorator
def group_delete(request,pk):
    model = Group.objects.get(pk=pk)
    model.delete()
    return redirect('group_list')

@login_required_decorator
def group_list(request):
    groups = service.get_group()
    ctx = {
        'groups':groups
    }
    return render(request,'groups/list.html',ctx)

@login_required_decorator
def student_create(request):
    model = Student()
    form = SubjectForm(request.POST or None,instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('student_list')
    ctx = {
        'form':form
    }
    return render(request,'students/form.html',ctx)

@login_required_decorator
def student_edit(request,pk):
    model = Student.objects.get(pk=pk)
    form = StudentForm(request.POST or None,instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('student_list')
    ctx = {
        'model':model,
        'form':form
    }
    return render(request,'students/form.html',ctx)

@login_required_decorator
def student_delete(request,pk):
    model = Student.objects.get(pk=pk)
    model.delete()
    return redirect('student_list')

@login_required_decorator
def student_list(request):
    students = service.get_student()
    ctx = {
        'students':students
    }
    return render(request,'students/list.html',ctx)

def dashboard_view(request):
    # 1. Bar Chart uchun: Har bir Kafedradagi o'qituvchilar soni
    kafedralar = Kafedra.objects.annotate(teacher_count=Count('teacher'))
    bar_labels = [k.name for k in kafedralar]
    bar_data = [k.teacher_count for k in kafedralar]

    # 2. Pie Chart uchun: Umumiy obyektlar nisbati
    pie_labels = ['Teachers', 'Faculties', 'Kafedras', 'Subjects', 'Groups']
    pie_data = [
        Teacher.objects.count(),
        Faculty.objects.count(),
        Kafedra.objects.count(),
        Subject.objects.count(),
        Group.objects.count(),
    ]

    # 3. Statistik kartalar uchun hisoblar
    teachers_count = Teacher.objects.count()
    groups_count = Group.objects.count()
    subjects_count = Subject.objects.count()
    kafedras_count = Kafedra.objects.count()

    context = {
        'teachers_count': teachers_count,
        'groups_count': groups_count,
        'subjects_count': subjects_count,
        'kafedras_count': kafedras_count,
        'bar_labels': json.dumps(bar_labels),
        'bar_data': json.dumps(bar_data),
        'pie_labels': json.dumps(pie_labels),
        'pie_data': json.dumps(pie_data),
    }
    return render(request, 'dashboard.html', context)
