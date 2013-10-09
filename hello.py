#!/user/bin/env python

import urllib
import urllib2
from cookielib import CookieJar

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

formValues = {
    "Email":"andreij6@gmail.com", 
    "Passwd":"@Stronger6"         
}

data = urllib.urlencode(formValues)

response = opener.open("https://mail.google.com/mail/u/0/?tab=wm#inbox", data)

print response.read()


