import platform
import os
from random import randrange
import time
print("                 Byenvini nan jwèt la \n1- peze a pou dekale a goch\n2- peze l pou dekale a dwat")
a0=(5,5)
a1=a0[1]
a2=-5
c=""
while (a1>=-5):
    b=""
    a3=a1
    while(a3<=5):
        b+="\n"
        a3+=1
    print(b+"\n"+c+"---|||---|||---|||---")
    time.sleep(2)
    if platform.system()=='Windows':
        os.system('cls')
    else:  
        os.system('clear')
    a1-=1
    if a1==-5:
        a1=5
        a2=randrange(-5,5)
        while(a2>-5):
            c+="\t\t"
            a2-=1

