import requests
from lxml.cssselect import CSSSelector
from lxml.html import fromstring

SITE = 'https://www.svenskaplatser.se/'

def links(url, selector):
    html = requests.get(SITE + url).content.decode()
    tree = fromstring(html)
    sel = CSSSelector(selector)
    return ((el.text, el.attrib['href']) for el in sel(tree))

for city, url in links('', '#main p:not(#intro) a'):
    for street, url in links(url, '#main li a'):
        print('%s,%s' % (city, street))
