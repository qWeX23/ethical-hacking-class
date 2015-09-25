import string
import urllib2


isURL = False
url=""
for line in urllib2.urlopen("http://www.cisco.com"):

    if "<a href" in line:
        if "//" in line:
            for char in line:
                if isURL==True and char!="\"":
                    url = url +char
                if char=="\"" and isURL==False:
                    isURL = True
                elif char=="\"":
                    isURL= False
                    url= url +"\n"
                    


