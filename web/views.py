from django.shortcuts import render

from .models import Contact
# Create your views here.


def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['phone']
        message = request.POST['contactMessage']
        contact = Contact(Name=name,Email=email,PhoneNumber=number,message=message)
        contact.save()
    return render(request,'web/index.html')


# def index(request):
#     context = {}
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         number = request.POST.get('phone')
#         message = request.POST.get('message')



        # if name and email and number and message:
        #     contact = Contact(Name=name, Email=email, PhoneNumber=number, Message=message)
        #     contact.save()
        #     context['success'] = True
        # else:
        #     context['error'] = "Please fill all the required fields"

    # return render(request,'web/index.html',context)
