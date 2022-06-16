from django.contrib import admin
from user_multichoice_app.models import user_info,player_info,user_player_choice
# Register your models here.
admin.site.register(user_info)
admin.site.register(player_info)
admin.site.register(user_player_choice)

# @admin.register(user_player_choice)
# class PersonAdmin(admin.ModelAdmin):
#     list_display = ("email", "get_name")

#     def get_name(self, obj):
#         return " , ".join([p.name for p in obj.name.all()])