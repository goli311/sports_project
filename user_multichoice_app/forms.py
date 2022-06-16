from cProfile import label
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from user_multichoice_app.models import user_info,user_player_choice,player_info


class userInfoform(forms.ModelForm):

    class Meta:
        model=user_info
        # fields='__all__'
        fields=['email',]
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email', 'required': 'true'}),          
        }
    
# class userMultichoiceform(forms.ModelForm):
#     name = forms.ModelMultipleChoiceField(
#             queryset=player_info.objects.all(),
#             widget=forms.CheckboxSelectMultiple
#             )
#     class Meta:
#         model=user_player_choice
#         fields=['name']

#         # widgets = {
#         #     'name':  forms.CheckboxSelectMultiple()            
#         # }

class PlayerChoiceTestForm(forms.Form):   
    
    def __init__(self, qs=None, *args, **kwargs):
        # print('kwargs:',**kwargs)
        # print('kwargs:',qs)
        super(PlayerChoiceTestForm, self).__init__(*args, **kwargs)
        if qs:            
            self.fields['name'] = forms.ModelMultipleChoiceField(queryset=qs, widget=forms.CheckboxSelectMultiple(attrs={'checked' : 'checked'}),label="Player Choices")
    
    # class Meta:
    #     model=user_player_choice
    #     fields=['name']

class PlayerChoiceUncheckedForm(forms.Form):   
    
    def __init__(self, qs=None, *args, **kwargs):
        super(PlayerChoiceUncheckedForm, self).__init__(*args, **kwargs)
        if qs:            
            self.fields['name'] = forms.ModelMultipleChoiceField(queryset=qs, widget=forms.CheckboxSelectMultiple(),label="Player Choices")