from django.http import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from user_multichoice_app.models import user_info,user_player_choice
from user_multichoice_app.forms import userInfoform,PlayerChoiceTestForm,player_info,PlayerChoiceUncheckedForm
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def index(request):
    
    form = userInfoform()
    context={
        'form':form
    }
    form_mail=request.POST.get('email')
    request.session['email'] = form_mail
    if request.method == 'POST':
        form = userInfoform(request.POST)
        print('request.POST:',)
        
        if form_mail:
            email_exists= user_info.objects.filter(email=form_mail)
            if email_exists:
                return redirect(reverse('user_multichoice_app:user_subscribe')) 

        if form.is_valid():
            form.save()   
            return redirect(reverse('user_multichoice_app:user_subscribe'))        
                    
        else:  
           
            context={
                'form':form
            }       
            return render(request,'user_multichoice_app/index.html',context)    
    return render(request,'user_multichoice_app/index.html',context)
  

def user_subscribe(request):
 
    email= request.session.get('email', None)
    # print('email:',email)
    
    all_players=player_info.objects.all() # all payers
    email_obj= get_object_or_404(user_info,email=email)   
    choice_obj= user_player_choice.objects.filter(email=email_obj)
    # print('choice_obj:',choice_obj)    
    if not choice_obj:
      
        form=PlayerChoiceUncheckedForm(all_players,auto_id=False)    
        if request.method == 'POST':   
            
            form = PlayerChoiceUncheckedForm(all_players,request.POST,auto_id=False)
         
            if form.is_valid():
               
                print('email_obj:',email_obj)                   
                players_name=form.cleaned_data.get('name')
                print('players_name:',players_name)
                instance=user_player_choice.objects.create(email=email_obj) #create user_player_choice new instance
                print('instance:',instance)
                instance.name.add(*players_name)   # set multiple choices to instance
                         
                # return HttpResponse('Success...........')
                # return render(request,'user_multichoice_app/index.html',context)
                messages.success(request, f'Choices Saved.........')
                return redirect(reverse('user_multichoice_app:user_subscribe'))
                # return redirect(reverse('user_multichoice_app:index'))         
            else:
                context={'form':form} 
            return render(request,'user_multichoice_app/index.html',context)      
            
        else:
            context={ 'form':form}           
            return render(request,'user_multichoice_app/index.html',context)    
    else:
       
        email_obj= get_object_or_404(user_info,email=email)
        player_choice_obj= user_player_choice.objects.get(email=email_obj) # get player_choice_obj
        queryset=player_choice_obj.name.all() # player_choice_obj -> all multiple choices
        queryset_ids=[i.id for i in queryset] # id list of queryset
       
        diff_queryset=all_players.difference(queryset) #get unique list or difference of two lists to get unselected choices
        form = PlayerChoiceTestForm(queryset,auto_id=False)  
        form2 = PlayerChoiceUncheckedForm(diff_queryset,auto_id=False)  
        
        context={'form':form,'form2':form2} 
        if request.method == 'POST':     
                form = PlayerChoiceTestForm(queryset,request.POST,auto_id=False)
                form2 = PlayerChoiceUncheckedForm(queryset,request.POST,auto_id=False)
                print('request.POST:',request.POST)
                players_name=request.POST.getlist('name')
                queryset_ids_str=[str(i) for i in queryset_ids] # to make value str of queryset_ids
                add_id=list(set(players_name)-set(queryset_ids_str)) # already selected choices removed
                player_choice_obj.name.add(*add_id) # set new choiced to instance
               
                
                remove_id=[i for i in queryset_ids if str(i) not in players_name] # already selected values added to remove selection in db 
                # print('remove_id:',remove_id)
                player_choice_obj.name.remove(*remove_id) # remove unselected choices          
                # return HttpResponse('Success............')      
                messages.success(request, f'Choices Saved.........')
                return render(request,'user_multichoice_app/index.html',context) 
                # return redirect(reverse('user_multichoice_app:index'))                

        return render(request,'user_multichoice_app/index.html',context)   


def send_mail1(request):
    # all_user_player_choices=user_player_choice.objects.all()
    # for i in all_user_player_choices:
    #     print("--------------------------")
    #     players_name=i.name.all()
    #     # print(players_name)
    #     for j in players_name:
    #         print(j)
    #     print("--------------------------")

    # subject = 'welcome to Test Project'
    # message = f"""Hello, User"""
    # email_from = settings.EMAIL_HOST_USER
    # recipient_list = ['hello@yopmail.com',]
    # send_mail(subject, message, email_from, recipient_list)
   
    return HttpResponse("Mail Sending View ..............")