# python parser.py
# HTML解析
import urllib.request

url = 'http://www.python-izm.com/'

opener = urllib.request.build_opener()
opener.add_handler = [(
    "User-agent",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; ja; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 ( .NET CLR 3.5.30729)"
)]

htmldata = opener.open(url)
print(htmldata.read().decode('UTF-8'))

htmldata.close()
opener.close()
