
# makes encryptions using secure hash -BJC - 9/23/15 -- a4script2.py
import hashlib
import base64
Continue = True


while Continue == True:
    Choice = raw_input("\n[E]ncode or [D]ecode?? or [Q]uit")
    print Choice
    if Choice =="E":
        Continue2 = True
        while Continue2 == True:
            Choice2 = raw_input("[B]ase64 or [M]D5 or [S]HA1")
            if Choice2 == "B":
                Continue2 = False
                Input  = raw_input("Enter string to be encrypted")
                Output = base64.b64encode(Input)
                print " \noutput is:"
                print Output
            elif Choice2 == "M":
                Continue2 = False
                print "\noutput is:"
                print base64.b64encode(hashlib.md5(raw_input("Enter string to be encrypted")).hexdigest())
                print "not done yet"
            elif Choice2 == "S":
                Continue2 = False
                print "\noutput is:"
                print base64.b64encode(hashlib.sha1(raw_input("Enter string to be encrypted")).hexdigest())
    elif Choice =="D":
         Input = raw_input("Enter string to be decrypted")
         Output = base64.b64decode(Input)
         print " \noutput is:"
         print Output
    elif Choice =="Q":
        print "closing"
        Continue = False
        
