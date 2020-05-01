from django.contrib import admin
from .models import Create_Class, Name_of_classes, Students, Payment
# Register your models here.

admin.site.register(Create_Class)
admin.site.register(Name_of_classes)
admin.site.register(Students)
admin.site.register(Payment)
