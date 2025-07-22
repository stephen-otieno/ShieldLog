from django.shortcuts import render,redirect
from .forms import RegisterForm,CustomLoginForm
from django.contrib import messages
from django.contrib.auth import  login



def index(request):
    return render(request,'index.htm')



def homepage(request):
    return render(request, 'homepage.htm')



# Login function
def login_page(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homepage')  # Redirect to the home page after successful login
    else:
        form = CustomLoginForm()

    return render(request, 'login.htm',{'form':form})



# Register function
def signup_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')
    else:
        form = RegisterForm()


    return render(request, 'signup.htm', {'form': form})

