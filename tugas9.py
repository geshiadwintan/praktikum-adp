import time
import os
from termcolor import cprint

teks = "Happy Eid 🌙        "  
lebar = 20   #lebar teks ditampilan layar
durasi = 20  #durasi scrolling teks dalam detik
jeda = 0.3  #jeda antar langkah

steps = int(durasi / jeda) #hitung berapa kali teks bergerak

#Menampilkan teks yg  digulirkan
for i in range(steps):
    start = i % len(teks) 
    scrolled = (teks + teks)[start:start+lebar] 
    os.system('cls')
    print("=" * (lebar + 4))
    
    if i % 2 == 0:
        cprint(scrolled, 'magenta', attrs=['bold'])
    else:
        cprint(scrolled, 'magenta', attrs=['dark'])
    print("=" * (lebar + 4))
    
    time.sleep(jeda)