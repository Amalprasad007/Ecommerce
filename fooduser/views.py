from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from .models import User,categorys,items,HotProfile,categorys,tempcart,orders,userregs,cmuser,admins,commensettings,msgtoadmin,msgtostore
from .dbset import upatestorelinf,hotelereg,additemsdb,addtempcart,addorder,usrreg,adacategorys,sentotadmins,edititemsdb,senttostore,upatesc
from .forms import RegistrationForm
from django.contrib import messages
from django.views.generic.base import ContextMixin
import datetime
from django.views.generic import TemplateView,ListView
from django.core.files.storage import FileSystemStorage
import sys
sys.setrecursionlimit(2000)
from django.utils.crypto import get_random_string
from django import template
from django.db.models import Q


from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

register = template.Library()




@register.simple_tag()
def multiply(qty, unit_price, *args, **kwargs):
    # you would need to do any localization of the result here
    return qty * unit_price

class YourView(ListView):
    template_name = 'books/acme_list.html'
    context_object_name = 'object_list'
    queryset = categorys.objects.all()

def userhome(request):
    
    carttmps=get_random_string(length=15)
    itms=items.objects.filter(sts="2")
    if request.method == 'POST':
            if addtempcart(request)==1:
               return redirect('viewcart')
            else:
                messages.error(request, "Something error.")
    if 'cartids' not in request.session:
            request.session['cartids']=carttmps
    else:
            carttmps = request.session.get('cartids')

    return render(request,'user/index.html',{'z': itms.all()})




def useritems(request,value):
     #bkid= request.GET.get('value', None)
     cats=categorys.objects.filter(id=value).values()
     ids=value
     itms=items.objects.filter(catsgry=value,sts="2")
     if request.method == 'POST':
            if addtempcart(request)==1:
               return redirect('useritems', value=ids)
            else:
                messages.error(request, "Something error.")

     return render(request,'user/itemlist.html',{'z': itms.all(),'cats':cats.get()['categorys']})
def usersearch(request):
     bkid= request.GET.get('value', None)
     #cats=categorys.objects.filter(id=bkid).values()
     ids=bkid
     itms=items.objects.filter(Q(items__startswith=bkid) | Q(cattxt__startswith=bkid),sts="2")
     if request.method == 'POST':
            if addtempcart(request)==1:
               return redirect('usersearch', value=ids)
            else:
                messages.error(request, "Something error.")

     return render(request,'user/search.html',{'z': itms.all(),'cats':bkid})
 
def viewcart(request):
      catstps=tempcart.objects.filter(cattempid=request.session.get('cartids'))
      if request.method == 'POST':
          if 'fduser' not in request.session:
            return redirect('userlogin')
          else:      
            totalamt=request.POST.get('ttlamt')
            request.session['ttamt']= totalamt
            if addorder(request)==1:
               return redirect('paymets')
            else:
        
                    messages.error(request, "Something error.")
      if request.method == 'GET':
                   delv=request.GET.get('del')
                   if delv is not None:
                        instance = tempcart.objects.get(id=delv)
                        instance.delete()
                   return render(request,'user/cartview.html',{'catitems': catstps.all()})
      else:
         return render(request,'user/cartview.html',{'catitems': catstps.all()})

def userlogin(request):
      context=''
      if request.method=="POST":
            username=request.POST.get('Username')
            password=request.POST.get('Password')
            sellers=cmuser.objects.filter(umail=username, upass=password ).values()
            if sellers.count() == 1:
                
                    current_user = sellers.get()['id']
                    request.session['fduser']= current_user
                    request.session['fdusrnam']= sellers.get()['unames']
                    return redirect('userhome')
            else:
                context ='Invalid email or password'
      return render(request,'user/logins.html',{'context': context})
def userlogout(request):
        if 'fduser' in request.session:
            del  request.session['fduser']
            del  request.session['fdusrnam']
            del  request.session['cartids']
            carttmps=get_random_string(length=15)
            request.session['cartids']=carttmps    
            return redirect('userlogin')     
        return render(request,'user/logins.html')

def userregister(request):
     if request.method == 'POST':
        if usrreg(request):
            return redirect('userlogin')
        else:
            messages.error(request, "Something error.")
        
     return render(request,'user/register.html')
def viewordrs(request):
      carttmps = request.session.get('fduser')
      catstps=tempcart.objects.filter(catstatus="2",catuser=carttmps)
     
      if request.method == 'GET':
                   delv=request.GET.get('del')
                   if delv is not None:
                        instance = tempcart.objects.get(id=delv)
                        instance.delete()
                   return render(request,'user/myorders.html',{'catitems': catstps.all()})
      else:
         return render(request,'user/myorders.html',{'catitems': catstps.all()})

def paymets(request):
    amts=request.session.get('ttamt')
    if request.method == 'POST':
        idsk=request.session.get('cartids')
        #instance = tempcart.objects.get(cattempid=idsk).
        tempcart.objects.filter(cattempid=idsk).update(catstatus="2",cathtsts="2")
       # instance.catstatus="2"
       # instance.catstatus="2"
       # instance.cathtsts="2"
        
       
        return redirect('proccess')
    return render(request,'payment/index.html',{'amts': amts})

def proccess(request):
    carttmps=get_random_string(length=15)
    request.session['cartids']=carttmps
    return render(request,'payment/proccess.html')



def adlogin(request):
     context=''
     if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            sellers=admins.objects.filter(adminemail=username, adminpass=password ).values()
            if sellers.count() == 1:
                
                    current_user = sellers.get()['id']
                    request.session['adminlog']= current_user
                    return redirect('adviewhotel')
     else:
                context ='Wrong credintials'
     return render(request,'admins/index.html', {'context': context})



def adviewhotel(request):
     if request.method == 'GET':
                
                   delk=request.GET.get('del')
                   if delk is not None:
                        instance = HotProfile.objects.get(id=delk)
                        instance.delete()
                        try:
                             items.objects.get(catsgry=delk)
                             instancei=items.objects.get(catsgry=delk)
                             instancei.sts="1"
                             instancei.save()       
                        except items.DoesNotExist:
                        
                        
                              pass
     cats=HotProfile.objects.values()
     return render(request,'admins/hotelinfo.html',{'catgris': cats.all()})

def adacategory(request):
      if request.method == 'POST':
        if adacategorys(request)==1:
           messages.success(request, "categroy added.")
        else:
            messages.error(request, "Something error.")
      return render(request,'admins/addcategroy.html')
  
  
def editacategory(request):
     delk=request.GET.get('edit')
     catsvl=commensettings.objects.filter(id=delk)
     if request.method == 'POST':
            carid=request.POST.get('catid')
            cats=request.POST.get('cat')
            if carid is not None:
                instance = categorys.objects.get(id=carid)
                instance.categorys=cats
                instance.save() 
                return redirect('adviewcat')
            else:
                messages.error(request, "Something error.")
     return render(request,'admins/Editcat.html',{'cats':catsvl.all()})  
  
def adacategorystr(request):
      if request.method == 'POST':
        if adacategorys(request)==1:
            return redirect('additems')
        else:
            messages.error(request, "Something error.")
      return render(request,'store/addcategroy.html')

def adviewcat(request):
    if request.method == 'GET':
                  
                   delk=request.GET.get('del')
                   if delk is not None:
                        instance = categorys.objects.get(id=delk)
                        instance.catsts="0"
                        instance.save()
                        try:
                             items.objects.get(catsgry=delk)
                             instancei=items.objects.get(catsgry=delk)
                             instancei.sts="1"
                             instancei.save()       
                        except items.DoesNotExist:
                        
                        
                              pass
    cats=categorys.objects.filter(catsts="1")
    return render(request,'admins/viewcat.html',{'catgris': cats.all()})





def htreg(request):
      request.session.clear()
      if request.method == 'POST':
        if hotelereg(request):
            return redirect('hotlogin')
        else:
            messages.error(request, "Something error.")
      return render(request,'store/index.html')

def hotlogin(request):
        
        context=''
        if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            sellers=HotProfile.objects.filter(email=username, password=password ).values()
            if sellers.count() == 1:
                
                    current_user = sellers.get()['id']
                    request.session['hotuser']= current_user
                    request.session['hotusrnam']= sellers.get()['hname']
                    request.session['storeusersts']= sellers.get()['paymentsts']
                    return redirect('hthome')
        else:
                context ='Wrong credintials'
              
        return render(request,'store/login.html', {'context': context})


def hthome(request):
  
      paysts=request.session['storeusersts'];  
      return render(request,'store/home.html',{'sts':paysts})

def htprofile(request):
    paysts=request.session['storeusersts'];  
    regpay=commensettings.objects.all().values()
    request.session['storepy']=regpay.get()['amounts']
    if request.method == 'POST':
        if upatestorelinf(request)==1:
            return  redirect('paymetstore')
            #messages.success(request, "info Updated.")
            
        else:
            messages.success(request, "Something error.")
            
    return render(request,'store/updatepro.html',{'sts':paysts, 'amt':regpay.all()})

def paymetstore(request):
    amts=request.session['storepy']
    if request.method == 'POST':
        idsk=request.session['hotuser']
        #instance = tempcart.objects.get(cattempid=idsk).
        HotProfile.objects.filter(id=idsk).update(paymentsts="1")
       # instance.catstatus="2"
       # instance.catstatus="2"
       # instance.cathtsts="2"
        
        request.session['storeusersts']="1"
        return redirect('proccessstore')
    return render(request,'payment/index.html',{'amts': amts})

def proccessstore(request):

    return render(request,'payment/proccess2.html')



def additems(request):
      cats=categorys.objects.filter(catsts=1)
      if request.method == 'POST':
        if additemsdb(request)==1:
              messages.success(request, "Item added")
        else:
              messages.error(request, "Something error.")
      return render(request,'store/additem.html',{'catgris': cats.all()})
def edititems(request,value):
      cats=categorys.objects.values()
      itms=items.objects.filter(id=value,sts="2")
      if request.method == 'POST':
        if edititemsdb(request,value)==1:
              messages.success(request, "Item Updated")
        else:
              messages.error(request, "Something error.")
      return render(request,'store/edititem.html',{'catgris': cats.all(), 'item':itms.all()})

def htiotemview(request):
      hotids=request.session.get('hotuser')
      if request.method == 'GET':
                   delv=request.GET.get('dav')
                   delk=request.GET.get('del')
                   if delv is not None:
                        instance = items.objects.get(id=delv)
                        instance.sts="1"
                        instance.save()
                   if delk is not None:
                        instance = items.objects.get(id=delk)
                        instance.delete()
      itms=items.objects.filter(hotid=hotids).values()
      return render(request,'store/itemlist.html',{'z': itms.all()})

def htorderview(request):
      hotids=request.session.get('hotuser')
      if request.method == 'GET':
                   delv=request.GET.get('up')
                   delk=request.GET.get('del')
                   if delv is not None:
                        instance = tempcart.objects.get(id=delv)
                        instance.cathtsts="3"
                        instance.catdelivey="Dispatched"
                        instance.save()
                        
                        
                   if delk is not None:
                        instance = tempcart.objects.get(id=delk)
                        instance.delete()
      itms=tempcart.objects.filter(cathotl=hotids,cathtsts="2").values()
      return render(request,'store/neworder.html',{'z': itms.all()})
def htorderup(request):
      hotids=request.session.get('hotuser')
      if request.method == 'GET':
                   delv=request.GET.get('otd')
                   delvr=request.GET.get('dlv')
                   delk=request.GET.get('del')
                   if delv is not None:
                        instance = tempcart.objects.get(id=delv)
                        instance.cathtsts="4"
                        instance.catdelivey="Delivered"
                        instance.save()
                   if delvr is not None:
                        instance = tempcart.objects.get(id=delv)
                        instance.cathtsts="5"
                        instance.catdelivey="Delivered"
                        instance.save()
                   if delk is not None:
                        instance = tempcart.objects.get(id=delk)
                        instance.delete()
      itms=tempcart.objects.filter(cathotl=hotids,cathtsts="3").values()
      return render(request,'store/uporder.html',{'z': itms.all()})
def Deliverd(request):
      hotids=request.session.get('hotuser')
      if request.method == 'GET':
                   delk=request.GET.get('del')
                   if delk is not None:
                        instance = tempcart.objects.get(id=delk)
                        instance.delete()
      itms=tempcart.objects.filter(cathotl=hotids,cathtsts="5").values()
      return render(request,'store/deliverd.html',{'z': itms.all()})
  
  
  
def msgtoadminstr(request):
      if request.method == 'POST':
        if sentotadmins(request)==1:
              messages.success(request, "Message sent successfully")
        else:
              messages.error(request, "Something error.")
      return render(request,'store/sentmsg.html')
def msgtostoread(request):
      cats=HotProfile.objects.values()  
      if request.method == 'POST':
        if senttostore(request)==1:
              messages.success(request, "Message sent successfully")
        else:
              messages.error(request, "Something error.")
      return render(request,'admins/sentmsg.html',{'store':cats})
  
  
def adinbox(request):
      cats=msgtoadmin.objects.values()  
      if request.method == 'GET':
                  
                   delk=request.GET.get('del')
                   if delk is not None:
                        instance = msgtoadmin.objects.get(id=delk)
                        instance.delete()
      return render(request,'admins/inbox.html',{'msg':cats})

def strinbox(request):
      cats=msgtostore.objects.values()  
      if request.method == 'GET':
                  
                   delk=request.GET.get('del')
                   if delk is not None:
                        instance = msgtostore.objects.get(id=delk)
                        instance.delete()
      return render(request,'store/inbox.html',{'msg':cats})
def scupdate(request):
      cats=commensettings.objects.get(id=1)
      if request.method == 'POST':
        if upatesc(request)==1:
              messages.success(request, "Upadated successfully")
        else:
              messages.error(request, "Something error.")
      return render(request,'admins/fee.html',{'msg':cats.amounts})

def storelogout(request):
        if 'hotuser' in request.session:
            del  request.session['hotuser']
            del  request.session['hotusrnam']
            del  request.session['storeusersts']
  
            return redirect('hotlogin')     
        return render(request,'store/logins.html')
def invoice(request,values):
        items=tempcart.objects.filter(cattempid=values)
        users=orders.objects.filter(odrrcart=values)
        #cust=orders.objects.    
        return render(request,'user/invoice.html',{'z':items.all(),'c':users.all()})