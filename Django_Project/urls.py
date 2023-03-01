from django.contrib import admin
from django.urls import path
from Admin_Panel import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.home,name="Home"),    
    # path('login/',views.login,name="Login"),
    path("login/",auth_views.LoginView.as_view(template_name='login.html'),name="Login"),
    path("logout/",auth_views.LogoutView.as_view(template_name='logout.html'),name="Logout"),
    path('register/',views.register,name="Register"),    
    path("profile/",views.profile,name="Profile"),

    #Employee url
    path('employee/', views.employee_list,name="list_emp"),
    path('add/',views.addEmployee,name="emp_add"),
    path('edit/<int:id>',views.editEmployee,name="emp_edit"),
    path('delete/<int:id>',views.deleteEmployee,name="emp_del"),

    #Designation url
    path('designation/', views.listDesignation, name="des_list"),
    path('add desigantion/', views.addDesignation, name="des_add"),
    path('edit Designation/<int:id>', views.editDesignation, name="des_edit"),
    path('delete designation/<int:id>', views.deleteDesignation, name="des_del"),

    #Technology url
    path('technology/', views.technology_list,name="tech_list"),
    path('add technology/',views.addTechnology,name="tech_add"),
    path('edit technology/<int:id>',views.editTechnology,name="tech_edit"),
    path('delete technology/<int:id>',views.deleteTechnology,name="tech_del"),

    #Project url
    path('project/', views.project_list,name='proj_list'), 
    path('add project/',views.addProject,name='proj_add'),
    path('edit project/<int:id>',views.editProject,name='proj_edit'),
    path('delete/<int:id>',views.deleteProject,name='proj_del'),

    
]


































# from Message import views
# urlpatterns = [
#     path('admin/',admin.site.urls),                  
#     path('',views.message,name="Message"),                  
#     path('success/',views.success,name="Success"),                  
#     path('info/',views.info,name="Info"),                  
#     path('error/',views.error,name="Danger"),                  
#     path('warning/',views.warning,name="Warning"),                  

#SQlite Registration
# urlpatterns = [
#     path('admin/',admin.site.urls),
#     path('',views.home,name="home"),# 127.0.0.1:8000/         
#     path('addData',views.addData,name="addData"),
#     path('updateData/<int:id>',views.updateData,name="updateData"),
#     path('deleteData/<int:id>',views.deleteData,name="deleteData"),
# ]


