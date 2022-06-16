from telnetlib import STATUS
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
    context={
        'form':form
    }
    return render(request,'user_detail_app/index.html',context)

def register_email(request):
#    print('in register_email.......  ')
   email = request.POST.get('email')
#    print("request.POST.get('email'):",request.POST.get('email'))
   email_exists= user_details.objects.filter(email=email)
   players_get= players.objects.all()
   players_get1=serializers.serialize('json', players_get)
   # all_palyers   
   data={
    'players_get':players_get1,
    }
   if email_exists:
        print('Email Exists...........',email)
        new_players_get1= players.objects.all().filter(status=True)
        # p_name=[i.name for i in players_get1]
        # print('p_name:',p_name)
        email_obj= get_object_or_404(user_details, email=email)
        players_get= player_choices.objects.all().filter(email=email_obj)
        # print('players_get:',players_get)
        exist_p_name=[i.name.name for i in players_get]
        # print('exist_p_name:',exist_p_name)     


        data=[]
        for i in players_get:
         
            players_get1={
                'name':i.name.name,
                'pk':i.name.pk,
                'status':i.choice_status,
            }
            data.append(players_get1)

        # If new player added, append new player data in list data
        for j in new_players_get1:
            if j.name not in exist_p_name:
                players_get2={
                'name':j.name,
                'pk':j.pk,
                'status':False,
                    }
                data.append(players_get2)
       
   else:
        # form.save()
        user=user_details(email=email)
        user.save()

        print('Email not Exists...........')
   
        players_get= players.objects.all().filter(status=True)
        data=[]
        for i in players_get:
            print(i.name)
            players_get1={
                'pk':i.pk,
                'name':i.name,
            }
            data.append(players_get1)

   return JsonResponse(json.dumps(data), safe=False)

def save_players(request):
    # print(request.POST)
    email = request.POST.get('email')
    palyers_data = json.loads(request.POST.get('palyers_data'))
    # print('email:',email,'\t palyers_data:',palyers_data)
    # print('palyers_data:',palyers_data)
    email_obj= get_object_or_404(user_details, email=email)
  
    for i in palyers_data:
        # print('i:',i)
        # print('id:',i.get('id'))
        player_status_id=i.get('status')
        try:
            # print('id:',i.get('id'))       
            # print('player_status_id:',player_status_id)
           
            player_obj = get_object_or_404(players, id=i.get('id'))
            # -----------------------------------------------------------------
            
            choices_exists=player_choices.objects.filter(email=email_obj,name=player_obj)     
            if choices_exists:
                update_choices= player_choices.objects.get(email=email_obj,name=player_obj)  
                # print('update_choices:',update_choices)
                if player_status_id:...
                    # print('choice updated:',player_obj.name)
                    # update_choices.choice_status=player_status_id
                    # update_choices.save()
                else:
                    print('choice deleted:',player_obj.name)
                    update_choices.delete()
            else:
                if player_status_id: 
                    created =player_choices(email=email_obj,name=player_obj,choice_status=player_status_id)
                    created.save()

        except Exception as e:
            print(e)               
    
    return HttpResponse("OK")


def subscribe(request,id):
    email=get_object_or_404(user_details,id=id)
    context={
        'email':email
    }
    return render(request,'user_detail_app/subscribe.html',context)