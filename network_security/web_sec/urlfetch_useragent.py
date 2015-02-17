import urllib2

url = "http://www.microsoft.com"

# define an empty dictionary
headers = {}

headers['User-Agent'] = "Googlebot"

request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request)

print response.read()
response.close()

