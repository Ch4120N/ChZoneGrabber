#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  ____  _____  _    _  ____  ____  ____  ____     ____  _  _     ___  _   _  __  __  ___   ___  _  _ 
# (  _ \(  _  )( \/\/ )( ___)(  _ \( ___)(  _ \   (  _ \( \/ )   / __)( )_( )/. |/  )(__ \ / _ \( \( )
#  )___/ )(_)(  )    (  )__)  )   / )__)  )(_) )   ) _ < \  /   ( (__  ) _ ((_  _))(  / _/( (_) ))  ( 
# (__)  (_____)(__/\__)(____)(_)\_)(____)(____/   (____/ (__)    \___)(_) (_) (_)(__)(____)\___/(_)\_)
######################################################################################################

##############################################################
# ChZoneGrabber : 	Advanced Ch4120N Zone-H Grabber Tool     #
# Author 	    : 	Ch4120N                                  #
# Version 	    : 	1.0.0                                    #
# GitHub 	    : 	https://github.com/Ch4120N/ChZoneGrabber #
##############################################################


import os
import sys
import re
import threading
import signal

try:
    import requests
    from colorama import Fore, init

    init(autoreset=True)
except ImportError:
    sys.exit('\n [ - ] Please install requirements libraries. Using commands below:\n' \
             '\t- python -m pip install colorama==0.4.6 requests>=2.32.5\n' \
             '\t- Or\n' \
             '\t- python -m pip install -r requirements.txt\n'
            )

from ui.banner import Banner, Menu
from ui.decorators import MsgDCR
from core.config_parser import read_cfg, write_cfg
from core.config import Config


class ChZoneGrabber:
    def __init__(self):
        self.clear_screen()
        Banner()
        if not os.path.exists(Config._config_file):
            MsgDCR.WarningMessage(f'Configuration file \'{Config._config_file}\' not found. Generating new ...')
            write_cfg()
            MsgDCR.InfoMessage(f'The \'{Config._config_file}\' file generated!')
        
        self.config = read_cfg()

        if self.config['ZHE'] and self.config['PHPSESSID']:
            self.data = {
                'ZHE': self.config['ZHE'],
                'PHPSESSID': self.config['PHPSESSID']
            }
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def prompt(self, RequestMessage: str):
        print(MsgDCR.InputMessage(RequestMessage), end='', flush=True)
        return input()
    
    def append_file(self, file_name: str, data: str):
        with open(file=file_name, mode='a+') as fw:
            fw.write(data)
    
    def run(self):
        while True:
            self.clear_screen()
            Banner()
            if not self.config['ZHE'] or not self.config['PHPSESSID']:
                MsgDCR.WarningMessage('Some required settings are missing. Please set ZHE and PHPSESSID in the \'Settings\' menu.\n')
            Menu()

            choose = int(self.prompt('Select [1-7]: '))

            if choose == 1:
                pass


if __name__ == '__main__':
    app = ChZoneGrabber()
    app.run()

