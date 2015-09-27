import string
import urllib2


isURL = False
url=""
finalURLlist=[]
#intinalize files

lab51 = open("lab5-1.txt","w")
lab41 = open("lab4-1.txt","w")
lab52 = open("lab5-2.txt","w")
lab53 = open("lab5-3.txt","w")

for line in urllib2.urlopen("http://www.cisco.com"):

    if "<a href" in line:
        #print all href lines to lab5-1.txt
        lab51.write(line)
        if "//" in line:
            for char in line:
                if isURL==True and char!="\"":
                    url = url +char
                if char=="\"" and isURL==False:
                    isURL = True
                elif char=="\"":
                    isURL= False
                    url2 = string.split(url,"/")
                    for writeurltofile in url2:    
                        lab41.write(writeurltofile+'\n')
                    for actualURL in url2:
                        i=0
                        if "." in actualURL:
                            if ".com"  in actualURL:
                                if actualURL not in finalURLlist:
                                      # print actualURL
                                       #print "<<<<adding this to list<<<"
                                       i=i+1
                                       finalURLlist.insert(i,actualURL)


i=0
finalURLlistCopy=[]
for url in finalURLlist:
   if url[:string.find(url,".com")+4] not in finalURLlistCopy:
          finalURLlistCopy.insert(i,  url[:string.find(url,".com")+4])


y=sorted(finalURLlistCopy)
for string in y:
    lab53.write('\n'+string)
    print string
print"check lab51.txt,lab41.txt,lab53.txt for incremental results"
lab51.close()
lab41.close()
lab52.close()
lab53.close()

