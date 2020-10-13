"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from adminapp.views import *
from publicapp.views import *
from userapp.views import *
from makerapp.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"registration/$",registration,name='registration'),
    url(r"about/$",about,name='about'),
    url(r"contact/$",contact,name='contact'),
    url(r'home/$',home,name="home"),
    url(r"login/$",login,name='login'),
    url(r"index/$",index,name='index'),
    url(r"reply/(?P<id>[0-9]+)",reply,name='reply'),
    url(r"view_all/$",view_all,name='view_all'),
    url(r"view/$",view,name='view'),
    url(r"view_makers/$",view_makers,name='view_makers'),
    url(r"view_registered/$",view_registered,name='view_registered'),
    url(r"view_users/$",view_users,name='view_users'),
    url(r"view_active/$",view_active,name='view_active'),
    url(r"uedit/$",uedit,name='uedit'),
    url(r"uinbox/$",uinbox,name='uinbox'),
    url(r"umessage/$",umessage,name='umessage'),
    url(r"uprofile/$",uprofile,name='uprofile'),
    url(r"m_message/$",m_message,name='m_message'),
    url(r"medit/$",medit,name='medit'),
    url(r"minbox/$",minbox,name='minbox'),
    url(r"mprofile/$",mprofile,name='mprofile'),
    url(r"logout/$",logout,name='logout'),
    url(r"delete/(?P<id>[0-9]+)",delete,name='delete')




]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

