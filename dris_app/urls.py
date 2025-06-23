#NAME: LEE KEI KAR
#STUDENT ID: 23100598

from django.urls import path
from . import views
from .views import custom_logout
from .views import user_logout, volunteer_logout
from .views import signup_view

urlpatterns = [
    path('', views.home, name='home'),
    path('disasters/', views.disaster_report_list, name='disaster_list'),
    path('aid-request/', views.submit_aid_request, name='aid_request'),
    path('my-submissions/', views.view_my_submissions, name='my_submissions'),
    path('logout/', custom_logout, name='logout'),
    path('citizen/shelters/', views.citizen_shelters_view, name='citizen_shelters'),
    path('volunteer/shelters/', views.volunteer_shelters_view, name='volunteer_shelters'),
    path('', views.citizen_home, name='citizen_home'),
    path('accounts/logout/', user_logout, name='user_logout'),
    path('volunteer/logout/', volunteer_logout, name='volunteer_logout'),
    path('signup/', signup_view, name='signup')
]