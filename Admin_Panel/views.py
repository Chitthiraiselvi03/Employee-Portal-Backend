from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import employee
from .forms import EmployeeForm
from .models import designation
from .forms import DesignationForm
from .models import technology
from .forms import TechnologyForm
from .models import project
from .forms import ProjectForm


# Create your views here.

def home(request):
    return render(request,"home.html")

def register(request):    
    if request.method=='POST':
        name=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]

        if password1==password2:        
            user=User.objects.create_user(username=name,email=email,password=password1)
            user.is_staff=True
            user.is_superuser=True
            user.save()
            messages.success(request,'Your account has been created! You are able to login')
            return redirect('Login')
        else:
            messages.warning(request,'Password Mismatching...!!!')
            return redirect('Register')        
    else:
        form=CreateUserForm()        
        return render(request,"register.html",{'form':form})
    
@login_required
def profile(request):
    return render(request,"profile.html")

def employee_list(request):
    mydict={}  
    emp=employee.objects.all()# select * from employee
    mydict['emp']=emp
    return render(request,"list_emp.html",mydict)

def addEmployee(request):
    mydict={}
    form=EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save() # insert into employee value('','')
        return redirect('/employee')       
    mydict['form']=form
    return render(request,"add_emp.html",mydict)

def editEmployee(request,id=None):
    one_emp=employee.objects.get(pk=id)
    mydict={}
    form=EmployeeForm(request.POST or None, instance=one_emp)
    if form.is_valid():
        form.save() 
        return redirect('/employee')       
    mydict['form']=form
    return render(request,"edit_emp.html",mydict)

def deleteEmployee(request,id=None):
    one_emp=employee.objects.get(pk=id)    
    one_emp.delete()
    return redirect('/employee')

def listDesignation(request):
    designation_list={}  
    records=designation.objects.all()
    designation_list['records']=records
    return render(request,"list_des.html",designation_list)

def addDesignation(request):
    designation_add={}
    form=DesignationForm(request.POST or None)
    if form.is_valid():
        form.save() 
        return redirect("/designation")       
    designation_add['form']=form
    return render(request,"add_des.html",designation_add)

def editDesignation(request,id=None):
    one_rec=designation.objects.get(pk=id)
    designation_edit={}
    form=DesignationForm(request.POST or None, instance=one_rec)
    if form.is_valid():
        form.save() 
        return redirect('/designation')       
    designation_edit['form']=form
    return render(request,"edit_des.html",designation_edit) 

def deleteDesignation(request,id=None):
    one_rec=designation.objects.get(pk=id)    
    one_rec.delete()
    return redirect('/designation')

def technology_list(request):
    mydict={}  
    tech=technology.objects.all()
    mydict['tech']=tech
    return render(request,"list_tech.html",mydict)

def addTechnology(request):    
    mydict={}
    form=TechnologyForm(request.POST or None)
    if form.is_valid():
        form.save() 
        return redirect('/technology')       
    mydict['form']=form
    return render(request,"add_tech.html",mydict)

def editTechnology(request,id=None):
    one_tech=technology.objects.get(pk=id)
    mydict={}
    form=TechnologyForm(request.POST or None, instance=one_tech)
    if form.is_valid():
        form.save() 
        return redirect('/technology')       
    mydict['form']=form
    return render(request,"edit_tech.html",mydict) 

def deleteTechnology(request,id=None):
    one_tech=technology.objects.get(pk=id)    
    one_tech.delete()
    return redirect('/technology')

def project_list(request):
    mydict={}
    proj=project.objects.all()
    mydict['proj']=proj
    return render(request,"list_proj.html",mydict)

def addProject(request):
    mydict={}
    form=ProjectForm(request.POST or None)
    if form.is_valid():
        form.save() 
        return redirect('/project')       
    mydict['form']=form
    return render(request,"add_proj.html",mydict)

def editProject(request,id=None):
    one_proj=project.objects.get(pk=id)
    mydict={}
    form=ProjectForm(request.POST or None, instance=one_proj)
    if form.is_valid():
        form.save() 
        return redirect('/project')       
    mydict['form']=form
    return render(request,"edit_proj.html",mydict)

def deleteProject(request,id=None):
    one_proj=project.objects.get(pk=id)    
    one_proj.delete()
    return redirect('/project')


    
