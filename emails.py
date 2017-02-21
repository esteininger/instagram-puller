import urllib2, ssl, json, re, sys

#add usernames
listUsers = ['iskra', 'fandemic', 'emglamguru']

def getEmail(account):
    url = 'https://www.instagram.com/' + account + '/?__a=1'
    context = ssl._create_unverified_context()
    response = urllib2.urlopen(url, context=context)
    for line in response:
        jsonContent = json.loads(line)
    bio = jsonContent['user']['biography']
    email = re.search(r'[\w\.-]+@[\w\.-]+', bio)
    try:
        return email.group(0)
    except:
        return False

def buildDict():
    dictUsers = []
    for user in listUsers:
        if getEmail(user):
            u = {}
            u['user'] = user
            u['email'] = getEmail(user)
            u['lead'] = False
            u['day'] = 0
            dictUsers.append(u)
    return dictUsers

print buildDict()
