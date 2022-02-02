from pygame import *
from time import *
def getdate():
    local_time=asctime(localtime(time()))
    return (local_time)
i=1
j=1
k=1
def eyes():
    
    sleep(5)
    mixer.init()
    mixer.music.load('e.ogg')
    mixer.music.play()
    a=str(input(""))
    if a=="eydone":
        mixer.music.stop()
    while mixer.music.get_busy():
        time.Clock().tick(10)
    with open("eyes.txt","a") as f:
        f.write(f"{getdate()} : Eyes exercise done {j} time\n")
    
def water():
    
    sleep(5)
    mixer.init()
    mixer.music.load('w.ogg')
    mixer.music.play()
    a=str(input(""))
    if a=="drank":
        mixer.music.stop()
    while mixer.music.get_busy():
        time.Clock().tick(10)
    with open("water.txt","a") as f:
        f.write(f"{getdate()} : Drank water  {i} time\n")
    

def physical():
    
    sleep(5)
    mixer.init()
    mixer.music.load('p.ogg')
    mixer.music.play()
    a=str(input(""))
    if a=="exdone":
        mixer.music.stop()
    while mixer.music.get_busy():
        time.Clock().tick(10)
    with open("physical.txt","a") as f:
        f.write(f"{getdate()} : Physical exercise done {k} time\n")
            

b=0
while(b<5):
    water()
    i+=1
    eyes()
    j+=1
    physical()
    k+=1