from django.utils import timezone


def select_word_form(number, singular, plural):
    if number == 1:
        return singular
    return plural


def get_time_ago(date):
    seconds = int((timezone.now() - date).total_seconds())
    if seconds <= 60:
        time = int(seconds)
        return select_word_form(time, '%i second ago', '%i seconds ago') % time     
    if seconds <= 3600:
        time = int(seconds / 60)
        return select_word_form(time, '%i minute ago', '%i minutes ago') % time
    if seconds <= 86400:
        time =  int(seconds / 3600)
        return select_word_form(time, '%i hour ago', '%i hours ago') % time
    time = int(seconds / 86400)
    return select_word_form(time, '%i day ago', '%i days ago') % time


def date_to_string(date):
    return date.strftime("%d %B %Y %H:%m:%S")


def make_short_dates(nicks):
    for nick in nicks:
        nick.date = get_time_ago(nick.date)
    return nicks


def make_long_dates(nicks):
    for nick in nicks:
        nick.date = date_to_string(nick.date)
    return nicks

