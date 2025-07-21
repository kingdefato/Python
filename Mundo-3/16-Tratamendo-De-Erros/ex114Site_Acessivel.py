import urllib
import urllib.error
import urllib.request
try:
    site = urllib.request.urlopen('http://www.youtube.com')
except urllib.error.URLError:
    print('\033[31mO site youtube não está acessível\033[m')
else:
    print('\033[32mO site youtube está acessível\033[m')