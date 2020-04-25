from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout , update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm , UserChangeForm , PasswordChangeForm
# Create your models here.


class Create_Class(models.Model):
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, default=1)
    class_name = models.CharField(max_length=150, null=True)
    from_choice = (
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    )
    from_days = models.CharField(max_length=10, choices=from_choice)
    to_days = models.CharField(max_length=10, choices=from_choice)
    from_time = models.TimeField()
    to_time = models.TimeField()
    created_on = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return f"/class/{self.pk}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"


class Name_of_classes(models.Model):
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, default=1, null=True)
    name = models.CharField(max_length=50, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

class StudentQuerySet(models.QuerySet):
    def search(self, query):
        lookup = (Q(name__icontains=query) |
                  Q(address__icontains=query) |
                  Q(parent_name__icontains=query)|
                  Q(course__class_name__icontains=query)
                  )

        return self.filter(lookup)


class StudentPostManager(models.Manager):
    def get_query_set(self):
        return StudentQuerySet(self.model, using=self._db)

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_query_set().search(query)


class Students(models.Model):
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, default=1, null=True)
    name = models.CharField(max_length=200, null=True)
    dob = models.DateField(null=True, verbose_name='Date of Birth')
    age = models.IntegerField()
    grade_choice = (
        ('G1', 'Grade-1'),
        ('G2', 'Grade-2'),
        ('G3', 'Grade-3'),
        ('G4', 'Grade-4'),
        ('G5', 'Grade-5'),
        ('G6', 'Grade-6'),
        ('G7', 'Grade-7'),
        ('G8', 'Grade-8'),
        ('G9', 'Grade-9'),
        ('G10', 'Grade-10'),
        ('G11', 'Grade-11'),
        ('G12', 'Grade-12'),
    )
    gender_choice=(
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'None'),
    )

    blood_choice=(
        ('O', 'O'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('A+', 'A+'),
        ('AB', 'AB'),
    )

    relation_choice=(
        ('Uncle', 'Uncle'),
        ('Aunty', 'Aunty'),
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Grandpa', 'Grandpa'),
        ('Grandma', 'Grandma'),
        ('Sister', 'Sister'),
        ('Brother', 'Brother'),
    )
    gender=models.CharField(choices=gender_choice, max_length=10, null=True)
    grade = models.CharField(choices=grade_choice, max_length=10, null=True)
    attending_school = models.CharField(max_length=100, null=True)
    course = models.ForeignKey(
        Create_Class, on_delete=models.SET_NULL, default=1, null=True)
    address = models.TextField(null=True)
    parent_name = models.CharField(max_length=200, null=True)
    parent_contact = models.CharField(max_length=20, null=True)
    parent_address = models.TextField(null=True)
    emerg_name = models.CharField(max_length=200, null=True, verbose_name='Emergency Name')
    emerg_contact = models.CharField(max_length=20, null=True, verbose_name='Emergency Contact')
    emerg_relation = models.CharField(choices=relation_choice ,max_length=20, null=True, verbose_name='Emergency Relationship')
    doc_name = models.CharField(max_length=200, null=False, default='None', verbose_name='Doctor Name')
    doc_contact = models.CharField(max_length=20, null=False, default='None', verbose_name='Doctor Contact')
    blood_type = models.CharField(choices=blood_choice,max_length=10, null=True)
    allergic = models.TextField(null=True)
    
    objects = StudentPostManager()


    def get_absolute_url(self):
        return f"/stds/{self.pk}"

    def get_edit_student(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_student(self):
        return f"{self.get_absolute_url()}/delete"