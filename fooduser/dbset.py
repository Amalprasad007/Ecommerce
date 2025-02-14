import datetime
from .models import HotProfile,cmuser,items,tempcart,orders,userregs,categorys,msgtoadmin,msgtostore,commensettings
from django.core.files.storage import FileSystemStorage
from django.utils.crypto import get_random_string
from django.utils.datastructures import MultiValueDictKeyError

import io as StringIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from html import escape

import random
def upatestorelinf(request):
    hid=request.session.get('hotuser')
    hotProfile=HotProfile.objects.get(id=hid)
    hotProfile.adrss=request.POST.get('hadrs')
    hotProfile.hname=request.POST.get('hname')
    hotProfile.place=request.POST.get('hplace')
    hotProfile.mobs=request.POST.get('hcnt')
    suss= hotProfile.save()
    return 1

def usrreg(request):
    UserProfile=cmuser()
    UserProfile.unames=request.POST.get('Username')
    UserProfile.upass=request.POST.get('Password')
    UserProfile.umail=request.POST.get('email')
    UserProfile.uphone=request.POST.get('Phone')
    suss= UserProfile.save()
    return 1
def hotelereg(request):
    hotProfile=HotProfile()
    hotProfile.email=request.POST.get('username')
    hotProfile.password=request.POST.get('password1')
    suss= hotProfile.save()
    return 1
def additemsdb(request):
    additm=items()
    additm.items=request.POST.get('iname')
    additm.price=request.POST.get('iprice')
    additm.qtys=request.POST.get('istock')
    additm.description=request.POST.get('idsicp')
    additm.catsgry=request.POST.get('icat')
    additm.cattxt=request.POST.get('cattxt')
    upload = request.FILES['iimg']
    fss = FileSystemStorage()
    file = fss.save(upload.name, upload)
    file_url = fss.url(file)
    additm.imgs=file_url
    additm.sts="2"
    additm.hotid= request.session.get('hotuser')
    suss= additm.save()
    return 1
def addtempcart(request):
    addtmp=tempcart()
    addtmp.cattempid=request.session.get('cartids')
    addtmp.cathots=request.POST.get('hotl')
    addtmp.catprice=request.POST.get('price')
    addtmp.catitm=request.POST.get('item_name')
    addtmp.catqty=request.POST.get('quantz')
    addtmp.catitids=request.POST.get('item_id')
    ids=request.POST.get('item_id')
    qtys=request.POST.get('quantz')
    addtmp.catimng=request.POST.get('img')
    addtmp.catstatus=1
    addtmp.catuser=request.session.get('fduser')
    addtmp.cathotl=request.POST.get('hotl')
    addtmp.catdelivey="Processing"
    addtmp.cathtsts="1"
    suss= addtmp.save()
    
    upitem=items.objects.filter(id=ids).values()
    qty=(int(upitem.get()['qtys']))-(int(qtys))
    obj=items.objects.get(id=ids)
    obj.qtys=qty
    obj.save()
    
    return 1

def addorder(request):
    ordersids=get_random_string(length=15)
    addodr=orders()
    addodr.odrid=ordersids
    addodr.odrrcart=request.session.get('cartids')
    addodr.odruser=request.session.get('fduser')
    addodr.odrdanam=request.POST.get('dname')
    addodr.oddrmob=request.POST.get('dmob')
    addodr.odrland=request.POST.get('dland')
    addodr.odrcity=request.POST.get('dcity')
    addodr.odrdlvey="Processing"
    random_num =  random.randint(2345678909800, 9923456789000)
    addodr.odridsa=random_num
    addodr.odrpaymet=1
    addodr.odrstatus=1
    suss= addodr.save()
    return 1
def reguser(request):
    adduser=userregs()
    adduser.useremail=request.POST.get('email')
    adduser.userpass=request.POST.get('Password')
    adduser.username=request.POST.get('Username')
    adduser.userphone=request.POST.get('Phone')
    adduser.usersts=1
    suss= adduser.save()
    return 1
def adacategorys(request):
    cat=categorys()
    cat.categorys=request.POST.get('cat')
    cat.catsts=1
    cat.save()
    return 1
def edititemsdb(request,ids):
    additm=items.objects.get(id=ids)
    additm.items=request.POST.get('iname')
    additm.price=request.POST.get('iprice')
    additm.qtys=request.POST.get('istock')
    additm.description=request.POST.get('idsicp')
  # additm.catsgry=request.POST.get('icat')
    file = request.FILES.get('iimg')
    if file and file.size > 0:
        upload = request.FILES['iimg']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        additm.imgs=file_url

    additm.sts="2"
    additm.hotid= request.session.get('hotuser')
    suss= additm.save()
    return 1

def sentotadmins(request):
    msg=msgtoadmin()
    msg.store=request.session['hotusrnam']
    msg.dates=datetime.date.today()
    msg.msg=request.POST.get('msg')
    msg.sts="1"
    suss= msg.save()
    return 1
def senttostore(request):
    msg=msgtostore()
    msg.store=request.POST.get('storeid')
    msg.dates=datetime.date.today()
    msg.msg=request.POST.get('msg')
    msg.sts="1"
    suss= msg.save()
    return 1
def upatesc(request):
    msg=commensettings.objects.get(id=1)
    msg.amounts=request.POST.get('cat')
    suss= msg.save()
    return 1

