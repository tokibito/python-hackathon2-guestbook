# coding: utf8
from django.contrib import admin

from guestbook.models import Greeting

class GreetingAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'create_at')

# Adminサイトへ登録する
admin.site.register(Greeting, GreetingAdmin)
