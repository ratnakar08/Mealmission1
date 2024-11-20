from django.shortcuts import render,redirect
from .models import food
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'base/home.html')

def org(request):
    foods = food.objects.filter(user=request.user)
    context = {'foods': foods}
    return render(request,'base/org.html',context)
def add(request):
    if request.method == 'POST':
        name = request.POST['name']
        expire = request.POST['expirdate']
        quantity = request.POST['quantity']
        food.objects.create(name=name,expirdate=expire,quantity=quantity,user=request.user)
        return redirect('base:org')
    return render(request,'base/add.html')
def delete(request):
    return