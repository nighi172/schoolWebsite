from django.db import models

# Create your models here.
class tbl_reg(models.Model):
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=50)
    DOB=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phno=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    typ=models.CharField(max_length=50,default="user")
    image=models.ImageField(upload_to='images',verbose_name='file',null=True,blank=True)
class tbl_cont(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    msg=models.CharField(max_length=100)
    regid=models.CharField(max_length=100,default="0")
    reply=models.CharField(max_length=100,default="Reply")
    replymessage=models.CharField(max_length=100,default="........")

class tbl_log(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100) 
    typ=models.CharField(max_length=50,default="user")
    