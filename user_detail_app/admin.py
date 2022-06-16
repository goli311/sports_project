from django.contrib import admin
from user_detail_app.models import players,user_details,player_choices
# Register your models here.
admin.site.register(players)
admin.site.register(user_details)
admin.site.register(player_choices)

# class playerAdmin(admin.ModelAdmin):
#     list_display = ('name', 'status')


# admin.site.register(players, playerAdmin)
