#!/usr/bin/env python3

import socket 
import os
import time
import sys


os.system('')

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class colors:
    red = '\033[91m'
    green = '\033[92m'
    blue = '\033[94m'
    yellow = '\033[93m'
    magenta = '\033[95m'
    cyan = '\033[96m'
    white = '\033[97m'
    bold = '\033[1m'
    underline = '\033[4m'
    black='\033[30m'
    Backsilver='\033[100m'
    silver='\033[90m'
    Backwhite='\033[3m'
    Backgreen='\033[42m'
    Backyellow='\033[43m'
    BackBlue='\033[44m'
    Backpink='\033[45m'
    Backcyan='\033[46m'
    BackRed='\033[41m'
    green = '\033[32m' 
    red = '\033[31m' 
    blue = '\033[36m' 
    pink = '\033[35m' 
    yellow = '\033[93m' 
    darkblue = '\033[34m' 
    white = '\033[00m'
    bluo = '\033[34m'
    red_p = '\033[41m'
    green_p = '\033[42m'
    bluo_p = '\033[44m'
    pink_p = '\033[45m'
    blue_p = '\033[46m'
    white_p = '\033[47m'
    rd = '\033[91m'
    black='\033[30m'
    bold = '\033[1m'
    underline = '\033[4m'
    magenta = '\033[95m'

class Handler:
    
    animatied = False
    
    def banner():
        return f"""
{colors.pink}    ______ _______ _______  _____  _______ _______
   |_____/ |______ |  |  | |     |    |    |______
   |    \_ |______ |  |  | |_____|    |    |______
 
 
                {colors.Backcyan}+{colors.white} {colors.yellow}Reverse Shell{colors.pink} {colors.Backcyan}+{colors.white}
                                                
{colors.white}
    """
    
    def usage():
        return """
"""

    def animated_print(msg):
        while Handler.animated_print:
            party = ['< ', '_', '^',' >']
            for item in party:
                print(f"\r{msg} {item}", end='')
                time.sleep(1)

    def binder(ip, port):
        pass
            
    def listener():
        pass
            
print(Handler.banner())



while 1:
    user = str(input(f"\n{colors.underline}Remote{colors.white} > "))
    
    text = user.split()
    
    if "help" in text:
        print(Handler.usage())
        
    elif "connect" in text:
        host = text[text.index('connect')+1].replace('host=', '')
        port = text[text.index('connect')+2].replace('port=', '')
        try:
            server.bind((host, int(port)))
            bindTime = time.strftime('%H:%M:%S')
            print(f'{colors.white}[{colors.green}{colors.bold}{bindTime}{colors.white}] [{colors.Backpink}info{colors.white}]{colors.yellow} server connected{colors.white}')
        except:
            notBindTime = time.strftime('%H:%M:%S')
            print(f'{colors.white}[{colors.green}{colors.bold}{notBindTime}{colors.white}] [{colors.BackRed}error{colors.white}]{colors.yellow} server cannot connected try again{colors.white}')
            pass
        
    elif "listen" in text:
        listenTime = time.strftime('%H:%M:%S')
        Handler.animatied = True
        server.listen(1)
        #Handler.animated_print(f'{colors.white}[{colors.green}{colors.bold}{listenTime}{colors.white}] [{colors.Backpink}info{colors.white}]{colors.yellow} remote on listener mode{colors.white}')

        global client
        client, addr = server.accept()
        acceptTime = time.strftime('%H:%M:%S')
        print(f'{colors.white}[{colors.green}{acceptTime}{colors.white}] [{colors.Backpink}info{colors.white}]{colors.yellow} client connected::{colors.green}{addr[0]}{colors.white}')
        
        if 'cmd' in text:
            print(f'{colors.white}[{colors.green}{acceptTime}{colors.white}] [{colors.Backpink}info{colors.white}]{colors.yellow} cmd mode is on{colors.white}')
            while 1:
                controller = str(input(f"\n{colors.underline}PS{colors.white} {colors.underline}Controller{colors.white} > "))
                client.send(controller.encode('ascii'))
                data = client.recv(1024).decode('ascii')
                print(data)
        else:pass
        
    elif 'exit' in text:
        sys.exit()