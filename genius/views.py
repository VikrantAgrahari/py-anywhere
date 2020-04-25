from django.shortcuts import render, get_object_or_404, redirect
from .models import Create_Class, Name_of_classes, Students
from .forms import (Creat_Class_Form, Create_Class_Model_Form,
                    Student_Model_Form)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from django.http import JsonResponse, HttpResponse
from datetime import datetime, date
import datetime as dt

from datetime import timedelta
from django.utils import timezone
# Create your views here.


def home(request):
    fieldname = 'class_name'
    to_bday, tmr_bday = Birthday_alert()
    #tmr_bday, to_bday = Birthday_alert()
    objs = Create_Class.objects.values(fieldname).order_by(
        fieldname).annotate(the_count=Count(fieldname))
    # print(objs)
    template_name = 'genius/home.html'
    context = {'head_title': "Little Genius",
               'data': 'Little Genius-School of Science & Technology',
               'count': objs,
               'tmr':tmr_bday,
               'to':to_bday,
               }
    return render(request, template_name, context)


def Add_name(request):
    if request.method == 'POST':
        print('JS got here')
        class_name = request.POST['class-name']
        print(class_name)
        data = None
        if len(class_name) > 0:
            is_there = Name_of_classes.objects.filter(name__iexact=class_name)
            if not is_there:
                inst = Name_of_classes.objects.create(name=class_name)
                data = {
                    'bool': True,
                    'msg': 'Created Successfully'
                }
            else:
                data = {
                    'bool': False,
                    'msg': 'Name already exists!'
                }
        else:
            data = {
                'bool': False,
                'msg': 'Name should not be empty!'
            }
        return JsonResponse(data)
    else:
        print('JS has not arrived')
        return redirect('/')


def Classes(request):
    objs = Create_Class.objects.all()
    names = Name_of_classes.objects.all()
    templatename = 'genius/classes.html'
    context = {'classes': objs, 'class': names}
    return render(request, templatename, context)

# @login_required(login_url='/login/')


def Class_create(request):
    form = Create_Class_Model_Form(request.POST or None)
    name = request.POST.get('select')
    fromday = request.POST.get('from_days')
    today = request.POST.get('to_days')
    fromtime = request.POST.get('from_time')
    to_time = request.POST.get('to_time')
    # get class_names from classname table
    fieldname = 'class_name'
    objs = Create_Class.objects.values(fieldname).order_by(
        fieldname).annotate(the_count=Count(fieldname))
    # Check whether data already exists in database
    already = Create_Class.objects.filter(
        class_name__iexact=name).filter(from_days__iexact=fromday).filter(to_days__iexact=today).filter(from_time__iexact=fromtime).filter(to_time__iexact=to_time)
    if not already:
        if name != "Click to select Class Name":
            if form.is_valid():
                obj = form.save(commit=False)
                obj.class_name = name
                #obj.created_by = request.user.username
                obj.save()
                print('successful')
                messages.success(request, 'Saved Successfully')
                form = Create_Class_Model_Form()
            else:
                #messages.error(request, 'Something wrong with data')
                form = Create_Class_Model_Form()

        else:
            messages.error(request, 'Please select the class name')
    else:
        messages.error(request, 'This class already exists')
    c_names = Name_of_classes.objects.values('name')
    templatename = 'genius/class_create.html'
    context = {'form': form, 'c_names': c_names, 'count': objs}
    return render(request, templatename, context)


def Class_Detail(request, id):
    objs = get_object_or_404(Create_Class, id=id)
    templatename = 'genius/class_detail.html'
    context = {'obj': objs, 'form': None}
    return render(request, templatename, context)


def Class_Update(request, id):
    obj = get_object_or_404(Create_Class, id=id)
    form = Create_Class_Model_Form(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'Class Updated Successfully.')
    templatename = 'genius/class_update.html'
    context = {'form': form,
               'head_title': f"Update {obj.class_name}",
               'title': f"Update : {obj.class_name}"}
    return render(request, templatename, context)


def Class_Delete(request, id):
    objs = get_object_or_404(Create_Class, id=id)
    templatename = 'genius/class_delete.html'
    if request.method == "POST":
        objs.delete()
        return redirect("/class")
    context = {'obj': objs, 'form': None}
    return render(request, templatename, context)


def Student_Main(request):
    objs= Students.objects.values().all()
    std_count=Students.objects.all().count()
    template_name = 'genius/students.html'
    context = {'head_title': 'Little Genius Students', 'students':objs,'count':std_count}
    return render(request, template_name, context)


def Student_Create(request):
    form = Student_Model_Form(request.POST or None)
    print('Student view came')
    cls=get_class_parent_detail()
    if request.method =='POST':
        # get class names and days
        for_age= form.data['dob']
        to_date=datetime.strptime(for_age, '%Y-%m-%d').date()
        get_age=Calculate_Age(to_date)
        print('MEthod is post')
        #now start storing the Student information
        print(form.data)
        if form.is_valid():
            print('form is valid')
            obj = form.save(commit=False)
            obj.age = get_age
            obj.save()
            messages.success(request, 'Student is registered successfully')
            form=Student_Model_Form()   
        else:
            messages.error(request,form.errors)
            print(form.errors)  
    template_name = 'genius/students_create.html'
    context = {'form': form,'classes':cls}
    return render(request, template_name, context)

def Student_Detail(request, id):
    objs = get_object_or_404(Students, id=id)
    templatename = 'genius/students_detail.html'
    context = {'obj': objs, 'form': None}
    return render(request, templatename, context)

def Student_Update(request, id):
    obj = get_object_or_404(Students, id=id)
    form = Student_Model_Form(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'Student Updated Successfully.')
        return redirect('/stds')
    templatename = 'genius/student_update.html'
    context = {'form': form,
               'head_title': f"Update {obj.name}",
               'title': f"Update : {obj.name}"}
    return render(request, templatename, context)

def Student_Delete(request, id):
    objs = get_object_or_404(Students, id=id)
    templatename = 'genius/students_delete.html'
    if request.method == "POST":
        objs.delete()
        messages.success(request,'Deleted Successfully.')
        return redirect("/stds")
    context = {'obj': objs, 'form': None}
    return render(request, templatename, context)


def get_class_parent_detail():
    classes= Create_Class.objects.values('pk','class_name','from_days','to_days','from_time','to_time').all()
    return classes

def Calculate_Age(bday):
    today = date.today() 
    age = today.year - bday.year - ((today.month, today.day) < (bday.month, bday.day)) 
    return age

def Birthday_alert():
    #students= Students.objects.all()
    datetime_now = timezone.now()
    now_day, now_month = datetime_now.day, datetime_now.month
    datetime_tomorrow = datetime_now + timedelta(days=1)
    tomorrow_day, tomorrow_month = datetime_tomorrow.day, datetime_tomorrow.month

    std_today = Students.objects.filter(dob__day=now_day, dob__month=now_month)
    std_tmr = Students.objects.filter(dob__day=tomorrow_day, dob__month=tomorrow_month)
    tday=[]
    tmr=[]

    for l in std_today:
        tday.append({
            'name':l.name,
            'course':l.course.class_name,
            'contact':l.parent_contact,
            'dob':l.dob
        })
    

    for l in std_tmr:
        tmr.append({
            'name':l.name,
            'course':l.course.class_name,
            'contact':l.parent_contact,
            'dob':l.dob
        })
   
    # putting into dictionary
    # for s in students:
    #     if s.dob == dt.date.today():
    #         to_bays.append({
    #             'name': 's.name',
    #             'course': 's.course.class_name',
    #             'dob' : 's.dob',
    #             'contact': 's.parent_contact',
    #         })
    #     elif s.dob + dt.timedelta(days=1) == tmr:
    #         tmr_bdays.append({
    #             'name': 's.name',
    #             'course': 's.course.class_name',
    #             'dob' : 's.dob',
    #             'contact': 's.parent_contact',
    #         })
    #     else:
    #         for m in students:
    #             print("else:",m.name)
    return (tday,tmr)
    

def Search(request):
    q= request.GET.get('q',None)
    print(q)
    results = Students.objects.search(query=q).values()
    std_count=Students.objects.all().count()
    template_name = 'genius/students.html'
    context = {'head_title': 'Little Genius Students', 'students':results,'count':std_count}
    return render(request, template_name, context)