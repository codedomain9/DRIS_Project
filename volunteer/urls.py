#NAME: LEE KEI KAR
#STUDENT ID: 23100598


from django.urls import path
from . import views
from .views import VolunteerLoginView

urlpatterns = [
    path('', views.volunteer_home, name='volunteer_home'),
    path('register/', views.register_skills, name='register_skills'),
    path('tasks/', views.view_tasks, name='view_tasks'),
    path('shelters/', views.view_shelters, name='view_shelters'),
    path('login/', VolunteerLoginView.as_view(), name='volunteer_login'),
    path('logout/', views.volunteer_logout, name='volunteer_logout'),
    path('signup/', views.volunteer_signup, name='volunteer_signup'),
]
