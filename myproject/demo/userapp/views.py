from django.shortcuts import render
from publicapp.models import * 
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def uedit(request):
    msg=""
    user=request.session["userid"]
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
        h=request.POST.get('t8')
        imag=request.FILES['img']
        if g==h:
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
            return HttpResponseRedirect(reverse('uprofile'))
        else:
            msg="password is not match"
     
    return render(request,"userapp/uedit.html",{"data":data,"msg":msg})

def uinbox(request):
    user1=request.session['userid']
    data=tbl_reg.objects.get(id=user1)
    data1=tbl_cont.objects.filter(regid=data.id)
    

    return render(request,"userapp/uinbox.html",{"data1":data1})

def umessage(request):
    msg=""
    user1=request.session['userid']
    data=tbl_reg.objects.get(id=user1)
    if request.method=='POST':
        a=data.name
        b=data.email
        c=request.POST.get('tb3')
        data1=tbl_cont.objects.create(name=a,email=b,msg=c,regid=user1)
        msg="send successfully"
    return render(request,"userapp/umessage.html",{"data":data,"msg":msg})

def uprofile(request):
    user1=request.session['userid']
    data=tbl_reg.objects.get(id=user1)
    return render(request,"userapp/uprofile.html",{"data":data})
