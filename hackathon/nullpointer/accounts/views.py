from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from base.models import UserProfile  
from django.contrib.auth.models import auth

# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        post = request.POST.get('option')

        print(f"Received data: {username}, {firstname}, {lastname}, {password1}, {password2}, {email}, {post}")

        # Check if all fields are filled
        if not all([username, firstname, lastname, password1, password2, email, post]):
            return render(request, 'accounts/register.html', {'error': "All fields are required."})

        # Check if passwords match
        if password1 != password2:
            return render(request, 'accounts/register.html', {'error': "Passwords do not match."})

        # Validate email format
        try:
            EmailValidator()(email)
        except ValidationError:
            return render(request, 'accounts/register.html', {'error': "Invalid email format."})

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html', {'error': "Username already exists."})

        if User.objects.filter(email=email).exists():
            return render(request, 'accounts/register.html', {'error': "Email already exists."})

        # Create user
        user = User.objects.create_user(username=username, password=password1, email=email, first_name=firstname, last_name=lastname)
        print(f"User created: {user}")

        # Create user profile
        user_profile = UserProfile.objects.create(user=user, post=post)
        print(f"User profile created: {user_profile}")

        # Redirect to login page after successful registration
        return redirect('accounts:login')  

    return render(request, 'accounts/register.html')



def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('base:home')
        else:
            message = {'message':"invalid cridentials"}
            return render(request,'accounts/loginpage.html',message)
    else:
        context={}
        return render(request,'accounts/loginpage.html',context)


def logoutpage(request):
    auth.logout(request)
    return redirect('base:home')