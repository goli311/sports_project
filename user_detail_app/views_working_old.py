from re import U
from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from user_detail_app.forms import *
from user_detail_app.models import user_details

# Create your views here.
def index(request):
    form = Subscriptionform()
    if request.method == 'POST':
        form = Subscriptionform(request.POST)
        if form.is_valid():
            # print('form:',form)
            email=form.cleaned_data['email']
            email_exists= user_details.objects.get(email=email)
            if email_exists:
                print('Email Exists...........',email)
                print('Email Exists...........',email_exists.id)
                # data={
                #     'email':email
                # }
                # return render(request,'user_detail_app/subscribe.html',data)
                # return redirect(reverse('user_detail_app:subscribe',args=(email_exists.id,)))
                return redirect(reverse(f'/subscribe/{email_exists.id}'))
               
            else:
                form.save()
                # user=form.save(commit=False)
                # user.subscribe_status=True
                # user.save()

                print('Email not Exists...........')
        else:
            # print ('form.errors:',form.errors)
            context={
                'form':form
            }
            return render(request,'user_detail_app/index.html',context)

    context={
        'form':form
    }
    return render(request,'user_detail_app/index.html',context)

def subscribe(request,id):
    email=get_object_or_404(user_details,id=id)
    context={
        'email':email
    }
    return render(request,'user_detail_app/subscribe.html',context)