from .models import Like

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def is_liked(request, nick_title):
    try:
        required_like = Like.objects.get(nick_title = nick_title, ip_address = get_client_ip(request))
    except Like.DoesNotExist:
        return False
    else: 
        return True 
