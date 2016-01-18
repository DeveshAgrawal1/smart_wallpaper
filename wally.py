import urllib
from PIL import Image
from BeautifulSoup import BeautifulSoup
import requests
import ctypes
from win32api import GetSystemMetrics

def findwall():
    url='http://photography.nationalgeographic.com/photography/photo-of-the-day/'
    response = requests.get(url)
    source=response.text.encode('ascii', 'ignore')
    soup=BeautifulSoup(source)
    for wall in soup.find('div',{'class':'primary_photo'}).findAll('img'):
        src=wall.get('src')
        scr= src[2:]
        urllib.urlretrieve('https://'+scr,'wallpaper.jpg')

def setwall():
    findwall()
    path='C:\Users\Devesh\Desktop\Scripts\wallpaper.jpg'
    im=Image.open(path)
    if im.size[0]!= GetSystemMetrics(0) or im.size[1]!=GetSystemMetrics(1):
        ch=raw_input('Image does not fit the required resolution, still want to continue?(Y/N) ')
        if ch=='Y' or ch=='y':
            SPI_SETDESKWALLPAPER = 20
            ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, path, 3)
            print 'Wallpaper changed'
        else:
            print 'Wallpaper not changed'
    else:
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, path, 3)

setwall()