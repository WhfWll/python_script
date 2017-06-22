import urllib2
import cookielib

cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
	print 'name = ' + item.name
	print 'value = ' + item.value
	print 'domain = ' + item.domain
	print 'path = ' + item.path
