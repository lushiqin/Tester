"""Tester URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from app.controller import accessToken,fromId,hostInfo,interfaceInfo,user,userInfo,wxInfo
from app.controller import Beautiful_Soup
from app.controller import index
from app.controller import book_bqg

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'',index.index),
    path(r'getOpenId',wxInfo.getOpenId),
    path(r'addUser',user.addUser),
    path(r'secAllUser',user.secAll),
    path(r'secOneUser',user.secOne),
    path(r'addUserInfo',userInfo.addUser),
    path(r'secAllInfo',userInfo.secAll),
    path(r'secOneInfo',userInfo.secOne),
    path(r'addFromId',fromId.addFromId),
    path(r'secOneFromId',fromId.secOne),
    path(r'addAccessToken',accessToken.saveDb),
    path(r'updateAccessToken',accessToken.updateDb),
    path(r'addHost',hostInfo.addHost),
    path(r'secAllHost',hostInfo.secAll),
    path(r'secOneHost',hostInfo.secOne),
    path(r'addInterface',interfaceInfo.addInterface),
    path(r'secAllInterface',interfaceInfo.secAll),
    path(r'secOneInterface',interfaceInfo.secOne),
    path(r'sendmsg',wxInfo.setmessage),
    path(r'xs84',Beautiful_Soup.xs84),
    path(r'xsml',Beautiful_Soup.xsml),
    path(r'xszj',Beautiful_Soup.xszj),
    path(r'xstest',Beautiful_Soup.xstest),
    path(r'bqghomepage',book_bqg.homePage),
    path(r'bqgtypecolumn',book_bqg.typeColumn),
    path(r'bqgcatalog',book_bqg.catalog),
    path(r'bqgdetails',book_bqg.details)

]
