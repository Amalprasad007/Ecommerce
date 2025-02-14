from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [

    
    path('', views.userhome, name="userhome"),
    path('items/<int:value>', views.useritems, name="useritems"),
    path('login', views.userlogin, name="userlogin"),
    path('logout', views.userlogout, name="userlogout"),
    path('register', views.userregister, name="userregister"),
    path('cartv', views.viewcart, name="viewcart"),
    path('payment', views.paymets, name="paymets"),
    path('procces', views.proccess, name="proccess"),
    path('usersearch', views.usersearch, name="usersearch"),
    path('myorders', views.viewordrs, name="viewordrs"),


    path('admin/', admin.site.urls),
    path('admins/', views.adlogin, name="adlogin"),
    path('admins/viewhotel', views.adviewhotel, name="adviewhotel"),
    path('admins/category', views.adacategory, name="adacategory"),
    path('admins/viewcattgry', views.adviewcat, name="adviewcat"),
    path('admins/editcat', views.editacategory, name="editacategory"),
    path('admins/sendmsg', views.msgtostoread, name="msgtostore"),
    path('admins/inbox', views.adinbox, name="adinbox"),
    path('admins/scupdate', views.scupdate, name="scupdate"),

    path('store/', views.htreg, name="htreg"),
    path('store/login', views.hotlogin, name="hotlogin"),
    path('store/home', views.hthome, name="hthome"),
    path('store/update', views.htprofile, name="htprofile"),
    path('store/additem', views.additems, name="additems"),
    path('store/addcats', views.adacategorystr, name="adacategorystr"),
    path('store/viewlist', views.htiotemview, name="htiotemview"),
    path('store/edititem/<int:value>', views.edititems, name="edititems"),
    path('store/neworder', views.htorderview, name="htorderview"),
    path('store/updateodr', views.htorderup, name="htorderup"),
    path('store/storepay', views.paymetstore, name="paymetstore"),
    path('store/payprog', views.proccessstore, name="proccessstore"),
    path('store/Deliverd', views.Deliverd, name="Deliverd"),
    path('store/sendmsg', views.msgtoadminstr, name="msgtoadminstr"),
    path('store/inbox', views.strinbox, name="strinbox"),
    path('store/logout', views.storelogout, name="storelogout"),
    path('store/invoice/<values>',views.invoice,name="myview")
    ]
    

urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)