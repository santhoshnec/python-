a=input()
l=['a','e','i','o','u','A','E','I','O','U']
if(a.isdigit()):
    print("invalid")
elif(a in l):
    print("vowel")
else:
    print("consonant")
   
