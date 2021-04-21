from django.shortcuts import render
from .forms import NewUserForm
from .models import User

def index(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {"users":user_list}
    return render(request,'appTwo/index.html', context=user_dict)

def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request,'appTwo/help.html',context=helpdict)

def users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'appTwo/users.html',{'form':form})
