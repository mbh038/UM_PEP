import json
import urllib

#url='http://python-data.dr-chuck.net/comments_42.json' # test
url='http://python-data.dr-chuck.net/comments_206671.json' # actual

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

data = json.loads(data)

#print json.dumps(data, indent=4)

total=0
count=0
for comment in data['comments']:
    count += 1
    total += int(comment['count'])  
print "Count =: ",count
print "Sum =: ",total