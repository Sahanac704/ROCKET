from lib2to3.fixes.fix_input import context
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CSIT
from .import global_message

# Create your views here.

def index(request):
    data = CSIT.objects.all()     #get all data from the database
    return render(request, template_name = "npjAirport/index.html", context = {'data' : data})

def table(request):
    data = CSIT.objects.filter(is_delete = False)
    return render(request, template_name= "npjAirport/table.html", context= {'data' : data})

def form(request):
    if request.method == 'POST':
        det = request.POST
        name = det.get('name')
        address = det.get('address')
        mobile = det.get('mobile')
        email = det.get('email')
        CSIT.objects.create(name = name, address = address, mobile = mobile, email = email)  #create method (ORM)
        messages.success(request, global_message.SUCCESS_MESSAGE)
        return redirect('/')

    return render(request, template_name = "npjAirport/form.html")


def edit(request, pk):

    if request.method == 'POST':
        det = request.POST
        name = det.get('name')
        address = det.get('address')
        mobile = det.get('mobile')
        email = det.get('email')

        dm = CSIT.objects.get(id = pk, is_delete = False)   #filter data as per given condition

        dm.name = name
        dm.address = address
        dm.mobile = mobile
        dm.email = email
        dm.save()
        messages.success(request, global_message.DELETE_MESSAGE)
        return redirect('/form')

    dt = CSIT.objects.get(id=pk)
    return render(request, template_name="npjAirport/edit.html", context = {'dt':dt})


def delete(request, pk):
    dx = CSIT.objects.get(id = pk, is_delete = False)
    dx.is_delete = True
    dx.save()
    messages.success(request, global_message.DELETE_MESSAGE)
    return redirect('/')



def contact(request):
    return render(request, template_name = "npjAirport/contact.html")