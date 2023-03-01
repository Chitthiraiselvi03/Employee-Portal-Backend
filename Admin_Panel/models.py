from django.db import models


# Create your models here.
class designation(models.Model):    
    designation=models.CharField(max_length=100)
    status=models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.designation}" 
    
class technology(models.Model):    
    technology=models.CharField(max_length=100)
    status=models.CharField(max_length=20)

    def __str__(self):
        return f"{self.technology}"    
    
class project(models.Model):
    project_name=models.CharField(max_length=100)
    technology=models.ForeignKey(technology,on_delete=models.CASCADE)    
    description=models.TextField(max_length=500)
    duration=models.IntegerField()
    duration_type=models.CharField(max_length=100,default='')
    
    def __str__(self):
        return f"{self.project_name}"    

class employee(models.Model):
    employee_name=models.CharField(max_length=100)
    designation=models.ForeignKey(designation,on_delete=models.CASCADE)
    project=models.ForeignKey(project,on_delete=models.CASCADE)
    gender=models.CharField(max_length=20)
    address=models.TextField(max_length=500)

   
    

    
    
        