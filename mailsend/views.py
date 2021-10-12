from django.shortcuts import render
from django.core.mail import * 

# Create your views here.


def doit(request):
    print(send_mail('Test mail via python','Hai there!!!!!!!!!!','zealoustechorptest@gmail.com',['skbss1224@gmail.com'],fail_silently=False))
