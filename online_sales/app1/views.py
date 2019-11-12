from django.shortcuts import render,redirect
from .models import MerchantModel
import random


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username == "admin" and password == "admin":
        return render(request, "welcome.html")
    else:
        return render(request, "index.html", {"mes": "Invalid Username or Password"})


def AddMerchant(request):
    auto_merchant_id = 0
    try:
        res = MerchantModel.objects.all()[::-1][0]
        auto_merchant_id = int(res.merchant_id) + 1
    except IndexError:
        auto_merchant_id = 100001
    return render(request, "addmerchant.html", {"data": MerchantModel.objects.all(), "mid": auto_merchant_id, "mpassword":'mpassword'})


def SaveMerchant(request):
    mid = request.POST.get("mid")
    mname = request.POST.get("mname")
    mcontact = request.POST.get("mcontact")
    memail = request.POST.get("memail")
    mpassword = random.randint(0000,9999)
    MerchantModel(merchant_id=mid,merchant_name=mname,merchant_contact=mcontact,merchant_email=memail,merchant_password=mpassword).save()
    return AddMerchant(request)


def logout(request):
    return render(request,"index.html")


def DeleteMerchant(request):
    dmid = request.POST.get("del_mid")
    MerchantModel.objects.filter(merchant_id=dmid).delete()
    return AddMerchant(request)