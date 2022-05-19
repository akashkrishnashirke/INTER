from django.shortcuts import render
from .forms import depaositForm
from .models import deposit_model

# Create your views here.

def depositView(request):
    form= depaositForm()
    md={'form':form}
    if request.method=='POST':
        form=depaositForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            mem = deposit_model.objects.all()
            dic = {'mem': mem}
            return render(request, 'deposit/member.html', context=dic)

    return render(request,'deposit/deposit.html',context=md)
def balance(request):
    bala=0


