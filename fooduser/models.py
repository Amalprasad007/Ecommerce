from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser

from django.db.models.deletion import SET_NULL
import os
import datetime

class User(AbstractUser):
    is_fuduser=models.BooleanField(default=False) 
    is_fudhotel=models.BooleanField(default=False) 
    is_fudadmin=models.BooleanField(default=False)

class HotProfile(models.Model):
    hname=models.CharField(max_length=250, null=True)
    place=models.CharField(max_length=250, null=True)
    adrss=models.CharField(max_length=250, null=True)
    email=models.CharField(max_length=250, null=True)
    mobs=models.TextField(max_length=10)
    hid=models.TextField(max_length=10)
    password=models.CharField(max_length=250, null=True)
    paymentsts=models.CharField(max_length=250, null=True)
    status=models.CharField(max_length=250, null=True)
class categorys(models.Model):
    categorys=models.TextField(max_length=10)
    catsts=models.TextField(max_length=10)

class items(models.Model):
    items=models.TextField(max_length=10)
    catsgry=models.CharField(max_length=250, null=True)
    cattxt=models.CharField(max_length=250, null=True)
    price=models.CharField(max_length=250, null=True)
    qtys=models.CharField(max_length=250, null=True)
    hotid=models.CharField(max_length=250, null=True)
    description=models.TextField(max_length=10)
    imgs=models.CharField(max_length=250, null=True)
    sts=models.CharField(max_length=250, null=True)
class cmuser(models.Model):
    unames=models.CharField(max_length=250, null=True)
    upass=models.CharField(max_length=250, null=True)
    umail=models.CharField(max_length=250, null=True)
    uphone=models.CharField(max_length=250, null=True)
class tempcart(models.Model):
    catitm=models.CharField(max_length=250, null=True)
    catprice=models.CharField(max_length=250, null=True)
    cathots=models.CharField(max_length=250, null=True)
    cattempid=models.CharField(max_length=250, null=True)
    catuser=models.CharField(max_length=250, null=True)
    catqty=models.CharField(max_length=250, null=True)
    catitids=models.CharField(max_length=250, null=True)
    catstatus=models.CharField(max_length=250, null=True)
    catimng=models.CharField(max_length=250, null=True)
    cathotl=models.CharField(max_length=250, null=True)
    catdelivey=models.CharField(max_length=250, null=True)
    cathtsts=models.CharField(max_length=250, null=True)
class orders(models.Model):
    odrid=models.CharField(max_length=250, null=True)
    odruser=models.CharField(max_length=250, null=True)
    odrrcart=models.CharField(max_length=250, null=True)
    odrpaymet=models.CharField(max_length=250, null=True)
    odrstatus=models.CharField(max_length=250, null=True)
    odrdlvey=models.CharField(max_length=250, null=True)
    odrdanam=models.CharField(max_length=250, null=True)
    oddrmob=models.CharField(max_length=250, null=True)
    odrland=models.CharField(max_length=250, null=True)
    odrcity=models.CharField(max_length=250, null=True)
    odrhotel=models.CharField(max_length=250, null=True)
    odridsa=models.CharField(max_length=250, null=True)

class userregs(models.Model):
    useremail=models.CharField(max_length=250, null=True)
    userphone=models.CharField(max_length=250, null=True)
    username=models.CharField(max_length=250, null=True)
    userpass=models.CharField(max_length=250, null=True)
    usersts=models.CharField(max_length=250, null=True)
class admins(models.Model):
    adminemail=models.CharField(max_length=250, null=True)
    adminpass=models.CharField(max_length=250, null=True)
class commensettings(models.Model):
    items=models.CharField(max_length=250, null=True)
    amounts=models.CharField(max_length=250, null=True)

class msgtoadmin(models.Model):
    store=models.CharField(max_length=250, null=True)
    dates=models.CharField(max_length=250, null=True)
    msg=models.CharField(max_length=250, null=True)
    sts=models.CharField(max_length=250, null=True)
class msgtostore(models.Model):
    store=models.CharField(max_length=250, null=True)
    dates=models.CharField(max_length=250, null=True)
    msg=models.CharField(max_length=250, null=True)
    sts=models.CharField(max_length=250, null=True)