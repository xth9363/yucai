from django.shortcuts import render,redirect
from main import models


# Create your views here.
def index(request):
    return_dict = {}
    products = models.Product.objects.filter(active=True, hot=True)
    newses = models.News.objects.filter(active=True)
    index_img = models.OtherImages.objects.get(code=1)
    logo = models.OtherImages.objects.get(code=2)
    company_name = models.OtherText.objects.get(code=1)
    company_name_2 = models.OtherText.objects.get(code=2)
    role_text = models.OtherText.objects.get(code=3)

    call_man = models.OtherText.objects.get(code=4)
    call_tel = models.OtherText.objects.get(code=5)
    call_email = models.OtherText.objects.get(code=6)
    call_address = models.OtherText.objects.get(code=8)
    about_us = models.OtherText.objects.get(code=9)


    print(index_img.content)
    return_dict["products"] = products
    return_dict["newses"] = newses
    return_dict["index_img"] = index_img
    return_dict["logo"] = logo
    return_dict["company_name"] = company_name
    return_dict["company_name_2"] = company_name_2
    return_dict["role_text"] = role_text
    return_dict["call_man"] = call_man
    return_dict["call_tel"] = call_tel
    return_dict["call_email"] = call_email
    return_dict["call_address"] = call_address
    return_dict["about_us"] = about_us

    return render(request, "index.html", return_dict)


def redirect_to(request):
    return redirect(request.GET.get("url"))
