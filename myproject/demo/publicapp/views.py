from django.shortcuts import render
from publicapp.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from datetime import date



# Create your views here.
def registration(request):
    msg=''
    if request.method=='POST':
        a=request.POST.get('t1')
        b=request.POST.get('t2')
        c=request.POST.get('t3')
        d=request.POST.get('t4')
        e=request.POST.get('t5')
        f=request.POST.get('t6')
        g=request.POST.get('t7')
        h=request.POST.get('t8')
        i=request.POST.get('t9')
        imag=request.FILES['img']
        if g==h:
            data=tbl_reg.objects.create(name=a,age=b,DOB=c,email=d,phno=e,address=f,password=g,typ=i,image=imag)
            data1=tbl_log.objects.create(username=d,password=g,typ=i)
            subject='Username & Password'
            message='Hello, your username is '+d+' and password is '+g+' .thank you'
            email_from=settings.EMAIL_HOST_USER
            recipientlist=[d,]
            send_mail(subject,message,email_from,recipientlist,fail_silently=True)
            msg='registration success'
        else:
            msg='password is not match' 

    return render(request,'publicapp/layout.html',{'msg':msg})


def about(request):
    return render(request,'publicapp/layout.html',{})

def contact(request):
    message=""
    if request.method=='POST':
        a=request.POST.get('tb1')
        b=request.POST.get('tb2')
        c=request.POST.get('tb3')
        data=tbl_cont.objects.create(name=a,email=b,msg=c,regid='0')
        message="SEND successfully"
    return render(request,'publicapp/layout.html',{'message':message})

def home(request):
    return render(request,"publicapp/layout.html",{})

def login(request):
    message=""
    if request.method=='POST':
        a=request.POST.get('t1')
        b=request.POST.get('t2')
        if tbl_log.objects.filter(username=a,password=b):
            data=tbl_log.objects.get(username=a,password=b)
            t=data.typ
            if t=="user":
                data1=tbl_reg.objects.get(email=a,password=b)
                uid=data1.id
                request.session['userid']=uid
                return HttpResponseRedirect(reverse('uprofile'))
            elif t=="maker":
                data2=tbl_reg.objects.get(email=a,password=b)
                mid=data2.id
                request.session['makerid']=mid
                return HttpResponseRedirect(reverse('mprofile'))
                
            elif t=="admin":
                data3=tbl_log.objects.get(username=a,password=b)
                aid=data3.id
                request.session["adminid"]=aid
                return HttpResponseRedirect(reverse('index'))
                
            else:
                message="invalid usertype"
        else:
            message="invalid username and password"
    return render(request,"publicapp/layout.html",{'message':message})

def logout(request):
    data=request.session.delete()
    return HttpResponseRedirect(reverse('login'))











