# def user_subscribe(request):
#     # email= request.session.get('email', None)
#     # if email:
#     #     email_exists= user_info.objects.filter(email=email)
#     #     if email_exists:
#     #         ...
#     # else:
#     #     return HttpResponse('Email Not found...........')    \
    
#     email= request.session.get('email', None)
#     # ---------------------------------------------------
#     email_obj= get_object_or_404(user_info,email=email)
#     a= user_player_choice.objects.get(email=email_obj)
#     queryset=a.name.all()
#     print('queryset:',a)
#     form = PlayerChoiceTestForm(queryset,request.POST)  
#     print(form)   
#     # ---------------------------------------------------
#     all_players=player_info.objects.all()
#     if email:
#         form=PlayerChoiceTestForm(all_players)    
#         if request.method == 'POST':
#             email_obj= get_object_or_404(user_info,email=email)
#             print('email_obj:',email_obj)
#             choice_obj= get_object_or_404(user_player_choice,email=email_obj)
#             print('choice_obj:',choice_obj)
#             if not choice_obj:
#                 form = PlayerChoiceTestForm(all_players,request.POST)
#                 # print(form)
#                 if form.is_valid():
#                     # print(form.cleaned_data)
#                     print('email_obj:',email_obj)                   
#                     players_name=form.cleaned_data.get('name')
#                     print('players_name:',players_name)
#                     instance=user_player_choice.objects.create(email=email_obj)
#                     print('instance:',instance)
#                     instance.name.add(*players_name)                  
#                     return HttpResponse('Success...........')
#                 else:
#                     context={'form':form} 
#                 return render(request,'user_multichoice_app/index.html',context)      
#             else:
                
#                 return render(request,'user_multichoice_app/index.html',context) 
#         # else:
#         #     return HttpResponse('Not POST Method...........')  
#     else:
#         return HttpResponse('Email Not found...........')
#     context={
#         'form':form
#     }           
#     return render(request,'user_multichoice_app/index.html',context)

# ---------------------------------------------
 # diff_exclude=all_players.exclude(id__in=[i.id for i in queryset])
        # print('diff_exclude:',diff_exclude)