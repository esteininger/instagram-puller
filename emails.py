import urllib2, ssl, json, re, urllib
import requests
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

URL = 'http://fashionista.com/2016/12/instagram-beauty-makeup-influencers-2016'

def getEmail(account):
    context = ssl._create_unverified_context()
    url = 'https://www.instagram.com/' + account + '/?__a=1'
    response = urllib2.urlopen(url, context=context)
    for line in response:
        jsonContent = json.loads(line)
    bio = jsonContent['user']['biography']
    email = re.search(r'[\w\.-]+@[\w\.-]+', bio)
    try:
        return email.group(0)
    except:
        return False

def buildDictionary():
    soup = BeautifulSoup(urllib2.urlopen(URL))
    starsLeads = []
    for x in soup.findAll('h3'):
        v = {}
        for y in x.findAll('a'):
            y = ''.join(map(str, y.contents))
            stars = y.split('@')
            v['email'] = getEmail(stars[1])
            print v['email']
        # for z in x:
        #     print z.string.split(',')
        starsLeads.append(v)
#     return starsLeads

buildDictionary()
