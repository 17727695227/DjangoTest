#__*__coding:utf-8__*__
from django.shortcuts import render
from . models import UserMessage

def getliuyan(request):
    # all_messages=UserMessage.objects.all()
    me=None
    all_messages = UserMessage.objects.filter(name='bobby',email='1@163.com')
    if all_messages:
        me=all_messages[0]
    # if request.method=='POST':
    #     name=request.POST.get('name','NAME')
    #     message=request.POST.get('message','MESSAGE')
    #     address=request.POST.get('address','ADDRESS')
    #     email=request.POST.get('email','')
    #
    #     user = UserMessage()
    #     user.name=name
    #     user.message=message
    #     user.email=email
    #     user.address=address
    #     user.save()

    return render(request,'liuyan.html',{'mymessage':me})

