from urllib.request import urlopen
from urllib.error import HTTPError

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

