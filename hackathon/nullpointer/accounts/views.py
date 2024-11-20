from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']


        if not all([username, firstname, lastname, password1, password2, email]):
            error = "All fields are required."
            return render(request, 'accounts/register.html', {'error': error})
        

        if password1 != password2:
            context = {'error': "you entered passwordes are not same "}
            return render(request,'accounts/register.html',context)
        

        if User.objects.filter(username=username).exists():
            context = {'error': "username already exists"}
            return render(request,'accounts/register.html',context)
        

        if User.objects.filter(email=email).exists():
            context = {'error': "Email already exists"}
            return render(request,'accounts/register.html',context)
        
        user = User.objects.create_user(username=username,password=password1,email=email,first_name=firstname,last_name=lastname)
        user.save();
        message = {'massage':"Successfully registered"}
        return render(request,'accounts:login',message)

    else:    
        return render(request,'accounts/register.html')


def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('base:index')
        else:
            message = {'message':"invalid cridentials"}
            return render(request,'accounts/loginpage.html',message)
    else:
        context={}
        return render(request,'accounts/loginpage.html',context)


def logoutpage(request):
    auth.logout(request)
    return redirect('base:index')