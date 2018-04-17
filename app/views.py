from django.shortcuts import render
from django.shortcuts import HttpResponse
from app import models

# Create your views here.
def UserCreat(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        models.UserInfo.objects.create(user=username,pwd = password)
        data={
            "msg":"请求成功",
            "data":{}
        }
        return HttpResponse(data)
    else:
        return HttpResponse("请求方式错误1")

def UserGet(request):
    data = {
        "msg":200,
        "data":models.UserInfo.objects.all()
    }
    if request.method == "GET":
        return render(request,"index.html",{"data":data})
    else:
        return HttpResponse("请求方式错误2")