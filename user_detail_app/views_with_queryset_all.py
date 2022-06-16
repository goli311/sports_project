from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from user_detail_app.forms import *
from user_detail_app.models import user_details,player_choices
from django.core import serializers
import json

# Create your views here.
def index(request):
    form = Subscriptionform()
    if request.method == 'POST':
        form = Subscriptionform(request.POST)
        if form.is_valid():
            # print('form:',form)
            email=form.cleaned_data['email']
            # email_exists=get_object_or_404(user_details,email=email)
            email_exists= user_details.objects.filter(email=email)
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
                # form.save()
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

def register_email(request):
   print('in register_email.......  ')
   email = request.POST.get('email')
   print("request.POST.get('email'):",request.POST.get('email'))
   email_exists= user_details.objects.filter(email=email)
   players_get= players.objects.all()
   players_get1=serializers.serialize('json', players_get)
   # all_palyers   
   data={
    'players_get':players_get1,
    }
   if email_exists:
        print('Email Exists...........',email)
        # players_get= player_choices.objects.all()
        # players_get1=serializers.serialize('json', players_get)
        # # all_palyers   
        # data={
        #     'players_get':players_get1,
        #     }
       
   else:
        # form.save()
        user=user_details(email=email)
        # user.subscribe_status=True
        user.save()

        print('Email not Exists...........')
   
   players_get= players.objects.all()
   for i in players_get:
       print(i.name)
   players_get1=serializers.serialize('json', players_get)
   # all_palyers   
   data={
    'players_get':players_get1,
    }
#    return HttpResponse('Success..............')
   return JsonResponse(json.dumps(data), safe=False)

def save_players(request):
    # print(request.POST)
    email = request.POST.get('email')
    palyers_data = json.loads(request.POST.get('palyers_data'))
    # print('email:',email,'\t palyers_data:',palyers_data)
    print('palyers_data:',type(palyers_data))
    email_obj= get_object_or_404(user_details, email=email)
    choice_exists= player_choices.objects.filter(email=email_obj)
    if choice_exists:
         print('Choice Exists...........')
        # # print('Email Exists...........',email)
       
        # # print('email_obj.id:',email_obj.id)
        # for i in palyers_data:
        #     # print('i:',i)
        #     # print('id:',i.get('id'))
        #     player_status=i.get('status')
        #     try:
        #         print('id:',i.get('id'))
        #         player_obj = get_object_or_404(players, id=i.get('id'))

        #         # if player_status == 1:
        #         #     players_save=player_choices.objects.update_or_create(email=email_obj,name=player_obj,choice_status=True)
        #         # else:
        #         #     players_save=player_choices.objects.update_or_create(email=email_obj,name=player_obj,choice_status=False)
        #         # players_save.save()
        #     except Exception as e:
        #         print(e)

               
    else:
        print('Choice not Exists...........')
        for i in palyers_data:
            # print('i:',i)
            # print('id:',i.get('id'))
            player_status=i.get('status')
            # if player_status == 1:
            try:
                print('id:',i.get('id'))
                player_obj = get_object_or_404(players, id=i.get('id'))
                if player_status == 1:
                    players_save=player_choices(email=email_obj,name=player_obj,choice_status=True)
                else:
                    players_save=player_choices(email=email_obj,name=player_obj,choice_status=False)
                players_save.save()
            except Exception as e:
                print(e)
    return HttpResponse("OK")


def subscribe(request,id):
    email=get_object_or_404(user_details,id=id)
    context={
        'email':email
    }
    return render(request,'user_detail_app/subscribe.html',context)