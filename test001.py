import urllib.request
import re

url = "https://www.baidu.com"
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read().decode(encoding = 'utf-8',errors = 'strict')
    return html

print(getHtml(url))

