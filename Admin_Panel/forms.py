from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import employee
from .models import designation
from .models import technology
from .models import project

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class EmployeeForm(forms.ModelForm):
    gen=('Male','Male'),('Female','Female')
    gender=forms.ChoiceField(choices=gen,widget=forms.RadioSelect)
    class Meta:
        model=employee
        fields=('employee_name','designation','project','gender','address') 

class DesignationForm(forms.ModelForm):

    state=('Active','Active'),('Inactive','Inactive')
    status=forms.ChoiceField(choices=state,widget=forms.RadioSelect)

    class Meta:
        model=designation
        fields=('designation','status') 

class TechnologyForm(forms.ModelForm):
    state=('Active','Active'),('Inactive','Inactive')
    status=forms.ChoiceField(choices=state,widget=forms.RadioSelect)
    
    class Meta:
        model=technology
        fields=('technology','status') 

class ProjectForm(forms.ModelForm):
    INTEGER_CHOICES= [tuple([x,x]) for x in range(1,32)]
    duration=forms.ChoiceField(choices=INTEGER_CHOICES, label="Duration", widget=forms.Select(), required=True),

    duration_type_Choice = [
        ('Week', 'Week'),
        ('Month', 'Month'),
        ('Year', 'Year'),
    ]
    duration_type = forms.ChoiceField(choices = duration_type_Choice, label="", initial='', widget=forms.Select(), required=True)

    
    class Meta:
        model=project
        fields=('project_name','technology','description','duration','duration_type')