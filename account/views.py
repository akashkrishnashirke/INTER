from django.shortcuts import render
from .models import account
from .forms import employee
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
def thanks(request,data):
    md1={'data':data}
    return render(request,'account/thank.html',context=md1)
def member(request):
    mem=account.objects.all()
    dic={'mem':mem}
    return render(request,'account/member.html',context=dic)

@login_required
def employeeform(request):
    form=employee()
    md={'form':form}
    if request.method=='POST':
        form=employee(request.POST)
        if form.is_valid():
            form.save(commit=True)
            #print(form.cleaned_data)
            mem = account.objects.all()
            dic = {'mem': mem}
            return render(request, 'account/member.html', context=dic)
            #return thanks(request,form.cleaned_data)


    return render(request,'account/employee.html',context=md)

@login_required
def home(request):
    return render(request,'account/home.html')





