# coding: utf8
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.views.generic.create_update import create_object

from guestbook.models import Greeting
from guestbook.forms import GreetingForm

def index(request):
    # 汎用ビューを利用
    return create_object(request,
                         form_class=GreetingForm,
                         post_save_redirect=reverse('guestbook_index'),
                         extra_context={'greeting_list': Greeting.objects.all()})

def index2(request):
    # 汎用ビューをを使わない場合
    # フォームオブジェクトを作成して入力内容の検証
    form = GreetingForm(request.POST or None)
    if form.is_valid():
        # 内容を保存してリダイレクト
        form.save()
        return HttpResponseRedirect(reverse('guestbook_index'))
    # 検証に失敗した場合はページを表示
    return render_to_response('guestbook/greeting_form.html',
                              {'greeting_list': Greeting.objects.all(),
                               'form': form})
