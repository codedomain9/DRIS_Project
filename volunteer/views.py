#NAME: LEE KEI KAR
#STUDENT ID: 23100598


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import VolunteerSkill
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import VolunteerSignUpForm


def volunteer_home(request):
    return render(request, 'volunteer/home.html')


@login_required
def register_skills(request):
    if request.method == 'POST':
        skill = request.POST.get('skill')
        availability = request.POST.get('availability')
        name = request.user.username  # ✅ only logged-in users allowed

        # Save to database
        VolunteerSkill.objects.create(
            name=name,
            skill=skill,
            availability=availability
        )

        messages.success(request, "Your skills have been registered.")
        return redirect('volunteer_home')

    return render(request, 'volunteer/register_skills.html')


@login_required
def view_tasks(request):
    from .models import VolunteerAssignment  # Import locally to avoid circular import

    # Find the volunteer skill record for this user
    volunteer = VolunteerSkill.objects.filter(name=request.user.username).first()

    # Get assigned tasks if the volunteer exists
    assignments = []
    if volunteer:
        assignments = VolunteerAssignment.objects.filter(volunteer=volunteer)

    return render(request, 'volunteer/view_tasks.html', {
        'assignments': assignments
    })


def view_shelters(request):
    return render(request, 'volunteer/view_shelters.html')

class VolunteerLoginView(LoginView):
    template_name = 'volunteer/volunteer_login.html'

    def get_success_url(self):
        return reverse_lazy('volunteer_home')


def volunteer_logout(request):
    logout(request)
    return redirect('volunteer_login')

def volunteer_signup(request):
    if request.method == 'POST':
        form = VolunteerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = VolunteerSignUpForm()
    return render(request, 'volunteer/signup.html', {'form': form})