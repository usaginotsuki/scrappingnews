import urllib.request
datos = urllib.request.urlopen('https://www.openwebinars.net').read().decode()
import sys
!{sys.executable} -m pip install beautifulsoup4