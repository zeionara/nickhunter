#from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from .models import Nick

def get_time_ago(date):
    seconds = int((timezone.now() - date).total_seconds())
    if seconds < 60:
        return '%i seconds ago' % int(seconds)
    elif seconds < 3600:
        return '%i minutes ago' % int(seconds / 60)
    elif seconds < 86400:
        return '%i hours ago' % int(seconds / 3600)
    else:
        return '%i days ago' % int(seconds / 86400)

def date_to_string(date):
    return date.strftime("%d %B %Y %H:%m:%S")

def index(request):
    latest_nicks = Nick.objects.order_by('-date')[:5]
    output = '<br/>'.join(['<b>%s</b> %s' % (nick.title, get_time_ago(nick.date)) for nick in latest_nicks])
    return HttpResponse(output)
    #return HttpResponse("Hello, world. You are in a <b>nickgenerator</b> index")

def details(request, nick_title):
    try:
        nick = Nick.objects.get(title = nick_title)
    except:
        return no_such_page(request)
    return HttpResponse("You're watching at nick '%s' which has been created %s" % (nick.title, date_to_string(nick.date)))


def no_such_page(request):
    return HttpResponse("404 - there is no such page on this site")

# Create your views here.
