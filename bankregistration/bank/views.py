from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .form import TaskForm
from .models import Districts,Branch

# Create your views here.
def login(request):
    if request.method == 'POST':
        luname=request.POST['name']
        lp=request.POST['password']
        user=auth.authenticate(username=luname,password=lp)
        if user is not None:
            auth.login(request,user)
            return redirect('bank:button')
        else:
            messages.info(request,"invalid credentials")
            return redirect('bank:login')

    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        uname=request.POST['username']
        p = request.POST['pass1']
        cp = request.POST['pass2']

        if p==cp:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'user name exists')
                return redirect('bank:register')

            else:
                user=User.objects.create_user(username=uname,password=p)
                user.save()
                print("user created")
                return redirect('bank:login')
        else:
           messages.info(request,"password not match")
           return redirect('bank:register')

    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def home(request):
    return render(request,'index.html')

def form(request):
    return render(request,'form.html')


def button(request):
    return render(request,'button.html')

def Submit(request):
    form = TaskForm()

    print(request)
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        f = request.POST.get('material')
        print(f)

        if form.is_valid():

            form.save()
            print('form saved')
            messages.success(request, 'Application Accepted.')
            return render(request, 'form.html', {'form': form.cleaned_data})
        else:
            print(form.errors)


    return render(request,'form.html',{'form':form})

def branches(request):
    branch_id = request.GET.get('branch_id')
    print(branch_id)
    cities =Branch.objects.filter(branch_id=branch_id)
    return render(request,'branch.html', {'cities':cities})