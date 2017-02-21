import urllib2, ssl, json, re, sys
context = ssl._create_unverified_context()
response = urllib2.urlopen(url, context=context)

query = 'beauty'
url = 'https://www.instagram.com/web/search/topsearch/?query=' + str(query)
dictUsers = []

def getEmail(account):
    url = 'https://www.instagram.com/' + account + '/?__a=1'
    for line in response:
        jsonContent = json.loads(line)
    bio = jsonContent['user']['biography']
    email = re.search(r'[\w\.-]+@[\w\.-]+', bio)
    try:
        return email.group(0)
    except:
        return False

for line in response:
    jsonContent = json.loads(line)['users']
    for u in jsonContent:
        username = u['user']['username']
        if getEmail(username):
            u = {}
            u['user'] = username
            u['email'] = getEmail(username)
            u['lead'] = False
            u['day'] = 0
            print u
            dictUsers.append(u)
            
print dictUsers
