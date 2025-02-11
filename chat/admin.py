from django.contrib import admin
from chat.models import User,Profile,  ChatMessage
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']


class ProfileAdmin(admin.ModelAdmin):
    list_editable = ['verified']
    list_display = ['user', 'full_name' ,'verified']


# Register your models here.
from .models import ChatMessage
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'reciever', 'message', 'is_read')
    list_editable = ['is_read']

admin.site.register(ChatMessage, ChatMessageAdmin)   
admin.site.register(User, UserAdmin)
admin.site.register( Profile,ProfileAdmin) 
