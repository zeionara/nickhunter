from django.utils import timezone

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

