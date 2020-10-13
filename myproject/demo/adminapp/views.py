from django.shortcuts import render
from publicapp.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
 



# Create your views here.
def index(request):
    admin1=request.session['adminid']
    return render(request,"adminapp/index.html",{})

def reply(request,id):
    data=tbl_cont.objects.get(id=id)
    admin1=request.session['adminid']
    if request.method=='POST':
        if data.reply=='Reply':
            a=request.POST.get("tb3")
            subject='REPLY'
            message=a
            email_from=settings.EMAIL_HOST_USER
            recipientlist=[data.email,]
            send_mail(subject,message,email_from,recipientlist,fail_silently=True)
            data.reply="Replied"
            data.replymessage=a
            data.save()
            return HttpResponseRedirect(reverse('view'))
    return render(request,"adminapp/reply.html",{"data":data})

def view_all(request):
    admin1=request.session['adminid']
    return render(request,"adminapp/view_all.html",{})

def view(request):
    data=tbl_cont.objects.all()
    return render(request,"adminapp/view_contact.html",{"data":data})


def view_makers(request):
    admin1=request.session['adminid']
    data=tbl_reg.objects.filter(typ="maker")
    return render(request,"adminapp/view_makers.html",{"data":data})

def view_registered(request):
    admin1=request.session['adminid']
    data=tbl_reg.objects.all()
    return render(request,"adminapp/view_registered.html",{"data":data})

def view_users(request):
    admin1=request.session['adminid']
    data=tbl_reg.objects.filter(typ="user")
    return render(request,"adminapp/view_users.html",{"data":data})

def view_active(request):
    admin1=request.session['adminid']
    data=tbl_log.objects.all()
    return render(request,"adminapp/view_active.html",{"data":data})

def delete(request,id):
    data=tbl_log.objects.get(id=id)
    data1=tbl_reg.objects.get(email=data.username,password=data.password).delete()
    data.delete()

    return HttpResponseRedirect(reverse('view_active'))
