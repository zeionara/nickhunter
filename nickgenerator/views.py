# standard

import random

# urllib

from urllib.request import urlopen
from urllib.error import HTTPError

# django

from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, redirect
from django.template import loader
from django.http import Http404

# local

from .models import Nick, Like
from .converters import get_time_ago, date_to_string, make_short_dates, make_long_dates
from .generators import get_new_nick
from .adapters import is_vk_free, is_github_free
from .utils import is_liked, get_client_ip, try_find_nick


def index(request):
    latest_nicks = make_short_dates(Nick.objects.order_by('-date')[:5])
    best_nicks = make_short_dates(Nick.objects.order_by('-rating')[:5])
    
    new_nick = get_new_nick()
    
    context = {
            'latest_nicks': latest_nicks, 
            'top_nicks': best_nicks, 
            'generated_nick': new_nick,
            'vk_free': is_vk_free(new_nick),
            'github_free': is_github_free(new_nick),
            'is_liked': is_liked(request, new_nick)
    }
    
    new_nick_object = Nick(title = new_nick, date = timezone.now())
    new_nick_object.save()

    return render(request, 'nickgenerator/index.html', context)


def details(request, nick_title):
    required_nick = try_find_nick(nick_title)
    
    latest_nicks = make_short_dates(Nick.objects.order_by('-date')[:5])
    best_nicks = make_short_dates(Nick.objects.order_by('-rating')[:5])

    context = {
            'latest_nicks': latest_nicks, 
            'top_nicks': best_nicks, 
            'generated_nick': required_nick.title,
            'vk_free': is_vk_free(required_nick.title),
            'github_free': is_github_free(required_nick.title),
            'date': required_nick.date,
            'rating': required_nick.rating, 
            'is_liked': is_liked(request, nick_title)
    }

    return render(request, 'nickgenerator/index.html', context)


def like(request, nick_title):
    required_nick = try_find_nick(nick_title)
    
    appendix = 1

    try:
        required_like = Like.objects.get(nick_title = nick_title, ip_address = get_client_ip(request))
    except Like.DoesNotExist:
        like = Like(nick_title = nick_title, ip_address = get_client_ip(request))
        like.save()
    else:
        required_like.delete() 
        appendix = -1

    required_nick.rating = required_nick.rating + appendix;
    required_nick.save()

    return redirect('nickgenerator:nick', nick_title = nick_title)


def latest(request):
    nicks = make_long_dates(Nick.objects.order_by('-date'))
    context = {'nicks': nicks, 'header': 'Latest nicks'}
    return render(request, 'nickgenerator/all.html', context)


def best(request):
    nicks = make_long_dates(Nick.objects.order_by('-rating'))
    context = {'nicks': nicks, 'header':'Best nicks'}
    return render(request, 'nickgenerator/all.html', context)


def no_such_page(request):
    return HttpResponse("404 - there is no such page on this site")

