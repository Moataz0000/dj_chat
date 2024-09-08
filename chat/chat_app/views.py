from django.shortcuts import render, redirect
from .forms import SingUpForm
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages



# @login_required(login_url='login')
def home(request):
    return render(request, 'chat/index.html')




def sign_up(request):
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Registration Successful.')
            return redirect('login')
    else:
        form = SingUpForm()

    return render(request, 'chat/sgin_up.html', {'form':form})            




def user_logout(request):
    logout(request)
    messages.success(request, 'Your\'er Logget out now.')
    return redirect('login')



def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)  
            messages.success(request, 'Login successfully.')
            return redirect('rooms')  
    else:
        form = AuthenticationForm()
    return render(request, 'chat/login.html', {'form': form})
