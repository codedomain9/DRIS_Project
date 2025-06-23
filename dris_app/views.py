#NAME: LEE KEI KAR
#STUDENT ID: 23100598


from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import DisasterReport, AidRequest
from .forms import AidRequestForm, DisasterFilterForm
from django.contrib.auth import logout
from .models import Shelter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm

User = get_user_model()

# View & filter disaster reports
def disaster_report_list(request):
    form = DisasterFilterForm(request.GET or None)
    reports = DisasterReport.objects.all()
    if form.is_valid():
        disaster_type = form.cleaned_data.get('disaster_type')
        if disaster_type:
            reports = reports.filter(disaster_type__icontains=disaster_type)
    return render(request, 'disaster_list.html', {'form': form, 'reports': reports})

# Submit aid request
@login_required
def submit_aid_request(request):
    if request.method == 'POST':
        form = AidRequestForm(request.POST)
        if form.is_valid():
            aid_request = form.save(commit=False)
            aid_request.user = request.user
            aid_request.save()
            return redirect('my_submissions')  # Redirect to optional view
    else:
        form = AidRequestForm()
    return render(request, 'aid_request.html', {'form': form})

# Optional: View My Submissions
@login_required
def view_my_submissions(request):
    my_reports = DisasterReport.objects.filter(user=request.user)
    my_requests = AidRequest.objects.filter(user=request.user)
    return render(request, 'my_submissions.html', {
        'my_reports': my_reports,
        'my_requests': my_requests
    })

def home(request):
    return render(request, 'home.html')

def custom_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'registration/logout.html')

def citizen_shelters_view(request):
    shelters = Shelter.objects.all()
    return render(request, 'citizen_shelters.html', {'shelters': shelters})

def volunteer_shelters_view(request):
    shelters = Shelter.objects.all()
    return render(request, 'volunteer_shelters.html', {'shelters': shelters})

def citizen_home(request):
    return render(request, 'home.html')


def user_logout(request):
    logout(request)
    return redirect('/accounts/login/')

# Clean logout for volunteers
def volunteer_logout(request):
    logout(request)
    return redirect('/volunteer/login/')

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # redirect to login page after signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})