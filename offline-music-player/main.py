import os,random,asyncio,keyboard
import threading,time
from playsound3 import playsound

file_count = 0
files=[]
play=True
first=True
stopped=False

with os.scandir('songs') as d:
    for e in d:
        e = str(e)
        e = e.replace("<DirEntry ", "")
        e = e.replace(">" ,"")
        e = e.replace("""'""","")
        files.append(e)
        file_count += 1

print(f"Total Files: {file_count}\n\n\n")
for i in files:
    print(i)
print("\n\n\n\n")



def shuffle():
    global first,play,stopped
    print("Playback started")
    random_song = random.choice(files)
    print("\nNow playing",random_song)
    sound = playsound(f'./songs/{random_song}',block=False)
    while True: 
        if sound.is_alive() == False and play == True:
            random_song = random.choice(files)
            sound = playsound(f'./songs/{random_song}',block=False)
            print("\nNow playing",random_song)
        elif play==False and stopped==False:
            print("Playback stopped")
            sound.stop()
            stopped=True
            

    print("play stopped")



def take_input():
    global play,stopped,first
    while True:
        cmd = input("\ncmd>")
        if cmd=="p":
            #print("status",play,stopped,first)
            if play==True:
                play=False
            elif play==False:
                play=True
                stopped=False
            
            time.sleep(3)
            

thread1 = threading.Thread(target=shuffle)
thread2 = threading.Thread(target=take_input)

thread1.start()
time.sleep(3)
thread2.start()

thread1.join()
thread2.join()
