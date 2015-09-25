import string
import urllib2


isURL = False
url=""
finalURLlist
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
                    url2 = string.split(url,"/")
                    for actualURL in url2:
                        if "." in actualURL:

                            break
                            
                    
                    
                    


