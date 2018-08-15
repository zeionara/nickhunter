import random

from urllib.request import urlopen
from urllib.error import HTTPError

#from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, redirect

from django.template import loader

from django.http import Http404

from .models import Nick

EVEN = ['b','c','d','f','g','h','j','k','l','m','n','p','r','s','t','v','x','z','q','ch','sh']
EVEN_LENGTH = len(EVEN)
ODD = ['a','e','i','o','u','w','y','ua','io','ia','oa']
ODD_LENGTH = len(ODD)
MIN_LENGTH = 3
MAX_LENGTH = 6

def is_404(url, sign):
    try:
        response = urlopen(url)
    except HTTPError:
        return True

    data = response.read()
    return sign in data.decode('utf-8')

def is_vk_free(nick):
    return is_404('http://vk.com/%s' % nick, 'error404')

def is_github_free(nick):
    return is_404('http://github.com/%s' % nick, '404')

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

def get_new_nick():
    next_odd = random.random() > 0.5;
    nick_length = random.randint(MIN_LENGTH, MAX_LENGTH)
    nick = ''
    for i in range(nick_length):
        if next_odd:
            nick = nick + ODD[random.randint(0, ODD_LENGTH - 1)]
        else:
            nick = nick + EVEN[random.randint(0, EVEN_LENGTH - 1)]
        next_odd = not next_odd
    return nick

def index(request):
    latest_nicks = Nick.objects.order_by('-date')[:5]
    best_nicks = Nick.objects.order_by('-rating')[:5]
    for nick in latest_nicks:
        nick.date = get_time_ago(nick.date)
    new_nick = get_new_nick()
    #template = loader.get_template("nickgenerator/index.html")
    context = {
            'latest_nicks': latest_nicks, 
            'top_nicks': best_nicks, 
            'generated_nick': new_nick,
            'vk_free': is_vk_free(new_nick),
            'github_free': is_github_free(new_nick)
    }
    
    new_nick_object = Nick(title = new_nick, date = timezone.now())
    new_nick_object.save()

    #return HttpResponse(template.render(context, request))
    return render(request, 'nickgenerator/index.html', context)
    
    #output = '<br/>'.join(['<b>%s</b> %s' % (nick.title, get_time_ago(nick.date)) for nick in latest_nicks])
    #return HttpResponse(output)
    
    #return HttpResponse("Hello, world. You are in a <b>nickgenerator</b> index")

def details(request, nick_title):
    try:
        required_nick = Nick.objects.get(title = nick_title)
    except Nick.DoesNotExist:
        raise Http404('Nick does not exist')
        #return no_such_page(request)
    
    
    latest_nicks = Nick.objects.order_by('-date')[:5]
    best_nicks = Nick.objects.order_by('-rating')[:5]
    for nick in latest_nicks:
        nick.date = get_time_ago(nick.date)
    #template = loader.get_template("nickgenerator/index.html")
    context = {
            'latest_nicks': latest_nicks, 
            'top_nicks': best_nicks, 
            'generated_nick': required_nick.title,
            'vk_free': is_vk_free(required_nick.title),
            'github_free': is_github_free(required_nick.title),
            'date': required_nick.date,
            'rating': required_nick.rating
    }

    #return HttpResponse(template.render(context, request))
    return render(request, 'nickgenerator/index.html', context)
    
    
    
    
    #return HttpResponse("You're watching at nick '%s' which has been created %s" % (nick.title, date_to_string(nick.date)))


def like(request, nick_title):
    try:
        required_nick = Nick.objects.get(title = nick_title)
    except Nick.DoesNotExist:
        raise Http404('Nick does not exist')

    required_nick.rating = required_nick.rating + 1;
    required_nick.save()

    return redirect('nickgenerator:nick', nick_title = nick_title)

def no_such_page(request):
    return HttpResponse("404 - there is no such page on this site")

# Create your views here.
