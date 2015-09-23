# Encodes and Decodes b64 -- BJC -- 9/22/15
import base64
Continue = True

while Continue == True:
    Choice = raw_input("\n[E]ncode or [D]ecode?? or [Q]uit")
    print Choice
    if Choice =="E":
        Input = raw_input("Enter string to be encrypted")
        Output = base64.b64encode(Input)
        print " \noutput is:"
        print Output
    elif Choice =="D":
         Input = raw_input("Enter string to be decrypted")
         Output = base64.b64decode(Input)
         print " \noutput is:"
         print Output
    elif Choice =="Q":
        print "closing"
        Continue = False
        
    
    
