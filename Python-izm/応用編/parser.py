# python parser.py
# HTML解析
import urllib.request

url = 'http://www.python-izm.com/'

htmldata = urllib.request.urlopen(url)
print(htmldata.read().decode('UTF-8'))

htmldata.close()
