from django.shortcuts import render
from publicapp.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def m_message(request):
    message=""
    maker1=request.session['makerid']
    data=tbl_reg.objects.get(id=maker1)
    if request.method=="POST":
        a=data.name
        b=data.email
        c=request.POST.get('t3')
        data1=tbl_cont.objects.create(name=a,email=b,msg=c,regid=maker1)
        message="send successfully"
    return render(request,"makerapp/m_message.html",{"data":data,"message":message})

def medit(request):
    user=request.session["makerid"]
    data=tbl_reg.objects.get(id=user)
    data1=tbl_log.objects.get(username=data.email,password=data.password)
    if request.method=="POST":
        a=request.POST.get('t1')
        b=request.POST.get('t2')
        c=request.POST.get('t3')
        d=request.POST.get('t4')
        e=request.POST.get('t5')
        f=request.POST.get('t6')
        g=request.POST.get('t7')
        imag=request.FILES['img']
        data.name=a
        data.age=b
        data.DOB=c
        data.email=d
        data.phno=e
        data.address=f
        data.password=g
        data.image=imag
        data.save()
        data1.username=d
        data1.password=g
        data1.save()
        return HttpResponseRedirect(reverse('mprofile'))
    return render(request,"makerapp/medit.html",{"data":data})
    

def minbox(request):
    maker1=request.session['makerid']
    data=tbl_reg.objects.get(id=maker1)
    data1=tbl_cont.objects.filter(regid=data.id)
    

    return render(request,"makerapp/minbox.html",{"data1":data1})

   

def mprofile(request):
    maker1=request.session['makerid']
    data=tbl_reg.objects.get(id=maker1)

    return render(request,"makerapp/mprofile.html",{"data":data})

