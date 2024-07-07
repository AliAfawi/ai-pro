from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import StudentSignUpForm, PractitionerSignUpForm

from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView


def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                if user.is_student:
                    return redirect('student_dashboard')
                elif user.is_practitioner:
                    return redirect('practitioner_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})








def student_register(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('student_dashboard')
    else:
        form = StudentSignUpForm()
    return render(request, 'registration/student_register.html', {'form': form})

def practitioner_register(request):
    if request.method == 'POST':
        form = PractitionerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('practitioner_dashboard')
    else:
        form = PractitionerSignUpForm()
    return render(request, 'registration/practitioner_register.html', {'form': form})



def home(request):
    return render(request, 'home.html')



from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .decorators import student_required, practitioner_required

@login_required
@student_required
def student_dashboard(request):
    return render(request, 'student_dashboard.html')

@login_required
@practitioner_required
def practitioner_dashboard(request):
    return render(request, 'practitioner_dashboard.html')





from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib import messages

def logout_user(request):
    auth_logout(request)
    return redirect('home')    






from django.urls import reverse_lazy




class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy('change_password')

    def form_valid(self, form):
        messages.success(self.request, 'Your password was successfully updated!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the error below.')
        return super().form_invalid(form)

