from django import forms
from .models import Create_Class, Name_of_classes, Students


class Creat_Class_Form(forms.Form):
    class_name = forms.CharField()
    from_days = forms.DateField()
    to_days = forms.DateField()
    from_time = forms.TimeField()
    to_time = forms.TimeField()


class Create_Class_Model_Form(forms.ModelForm):
    class Meta:
        model = Create_Class
        exclude = ['created_by', 'created_on','class_name']
        fields = ['class_name', 'from_days', 'to_days', 'from_time', 'to_time']
        # names = Name_of_classes.objects.values_list('name').distinct()
        #classname = list(names)
        from_choice = [
            ('Mon', 'Monday'),
            ('Tue', 'Tuesday'),
            ('Wed', 'Wednesday'),
            ('Thu', 'Thursday'),
            ('Fri', 'Friday'),
            ('Sat', 'Saturday'),
            ('Sun', 'Sunday'),
        ]
        # print('\nType is :')
        # print(type(from_choice))
        # print(classname)
        widgets = {
            #'class_name': forms.TextInput(attrs={'class': 'form-control'}),
            'from_days': forms.DateTimeInput(attrs={'class': 'from-date form-control'}),
            'to_days': forms.DateTimeInput(attrs={'class': 'from-date form-control'}),
            'from_time': forms.DateTimeInput(attrs={'class': 'from-time form-control'}),
            'to_time': forms.DateTimeInput(attrs={'class': 'from-time form-control'}),
        }


class Student_Model_Form(forms.ModelForm):
    class Meta:
        model = Students
        fields = ('__all__')
        exclude = ('created_by', 'age')
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
        blood_choice=(
        ('O', 'O'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('A+', 'A+'),
        ('AB', 'AB'),
    )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateTimeInput(attrs={'class': 'datetime-input form-control'}),
            'grade': forms.Select(choices=grade_choice, attrs={'class': 'form-control'}),
            'attending_school': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'gender': forms.Select(choices=gender_choice, attrs={'class': 'form-control'}),
            'parent_name':forms.TextInput(attrs={'class': 'form-control'}),
            'parent_contact': forms.TextInput(attrs={'class': 'form-control'}),
            'parent_address': forms.Textarea(attrs={'class': 'form-control', 'rows':3}),
            'emerg_name': forms.TextInput(attrs={'class': 'form-control'}),
            'emerg_contact':forms.TextInput(attrs={'class': 'form-control'}),
            'emerg_relation': forms.Select(choices=relation_choice,attrs={'class': 'form-control'}),
            'doc_name': forms.TextInput(attrs={'class': 'form-control'}),
            'doc_contact': forms.TextInput(attrs={'class': 'form-control'}),
            'blood_type':forms.Select(choices=blood_choice,attrs={'class': 'form-control'}),
            'allergic': forms.Textarea(attrs={'class': 'form-control', 'rows':3}),
        }
    def __init__(self, *args, **kwargs):
        super(Student_Model_Form, self).__init__(*args, **kwargs)
        self.fields['course']=forms.ModelChoiceField(queryset=Create_Class.objects.all(), label='Select Class', widget=forms.Select(attrs={'class':'form-control'}),help_text='If you are facing in choosing Class, detail is avaiable below.')