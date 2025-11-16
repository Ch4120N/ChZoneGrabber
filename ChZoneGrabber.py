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
import time
import threading
import signal
from datetime import datetime

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
        signal.signal(signal.SIGINT, self.exit_on_sigint)
        self.clear_screen()
        Banner()
        if not os.path.exists(Config._config_file):
            MsgDCR.WarningMessage(f'Configuration file \'{Config._config_file}\' not found. Generating new ...')
            write_cfg()
            MsgDCR.InfoMessage(f'The \'{Config._config_file}\' file generated!')
        
        self.config = read_cfg()
        self.output_dir = self.config['output_dir']
        self.time_date = self.config['time_date']
        self.data = None

        self.check_required_configs()
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def exit_on_sigint(self, frm, func):
        print('\n')
        MsgDCR.FailureMessage('Program Terminated By User!')
        sys.exit(2)
    
    def prompt(self, RequestMessage: str):
        print(MsgDCR.InputMessage(RequestMessage), end='', flush=True)
        return input()
    
    def back2menu_prompt(self):
        print('\n')
        self.prompt(f'Press {Fore.LIGHTBLUE_EX}[ {Fore.LIGHTRED_EX}ENTER {Fore.LIGHTBLUE_EX}]{Fore.LIGHTWHITE_EX} key for back to menu ...')
    
    def append_file(self, file_name: str, data: str):
        with open(file=file_name, mode='a+') as fw:
            fw.write(data)
    
    def time_now(self):
        return datetime.now().strftime("%Y-%m-%d_%H-%M")
    
    def banner(self):
        self.clear_screen()
        Banner()
    
    def check_required_configs(self):
        self.config = read_cfg() # Read Config.cfg file again
        if self.config['ZHE'] and self.config['PHPSESSID']:
            self.data = {
                'ZHE': self.config['ZHE'],
                'PHPSESSID': self.config['PHPSESSID']
            }
        
        if not os.path.exists(self.config['output_dir']):
            os.makedirs(self.config['output_dir'], exist_ok=True)
    
    def request_zone(self, file_name: str, url: str, pages: int, shown_name: str):
        try:
            response = requests.get(url=url, cookies=self.data)
            response_content = response.content.decode()
            MsgDCR.SectionMessage(f'Fetching Zone-H {shown_name} pages {pages}: {url}')
            urls = re.findall('<td>(.*)\n\s+</td>', response_content)
            if '/mirror/id/' in response_content:
                for url in urls:
                    filtered_url = url.replace('...', '')
                    correct_url = filtered_url.split('/')[0]
                    MsgDCR.GeneralMessage(f'-  {(correct_url)}')
                    self.append_file(file_name, f'https://{correct_url}\n')
        except (requests.RequestException, requests.ConnectionError, requests.ConnectTimeout) as ex:
            MsgDCR.FailureMessage(f'Connection failed. Please check your connection: {ex}')
        
    def run(self):
        while True:
            self.banner()
            self.check_required_configs()
            if not self.data:
                MsgDCR.WarningMessage('Some required settings are missing. Please set ZHE and PHPSESSID in the \'Settings\' menu.\n')
            Menu()

            choose = int(self.prompt('Select [1-7]: '))

            if choose == 1:
                self.grab_archives()
            elif choose == 2:
                self.grab_specials()
            elif choose == 3:
                self.grab_onholds()
            elif choose == 4:
                self.grab_notifier()
            elif choose == 5:
                self.change_settings()
            elif choose == 6:
                MsgDCR.FailureMessage('Program Terminated By User!')
                sys.exit(2)

    def change_settings(self):
        self.banner()
        output_dir = self.prompt('Enter path of output directory (e.g, reports/ , Default): ').replace('\\', '/')

        if not output_dir or output_dir == '':
            output_dir = 'reports/'
        
        self.banner()
        time_date = self.prompt('Do you want the date and time to be included in the file name? (Y/n): ').lower()
 
        if not time_date or time_date == '':
            time_date = True
        
        elif not time_date in ['y', 'yes', 'n', 'no']:
            MsgDCR.FailureMessage('Please enter valid input (e.g, y/n)')
            self.back2menu_prompt()
            self.change_settings()
        elif time_date in ['y', 'yes']:
            time_date = True
        elif time_date in ['n', 'no']:
            time_date = False
        
        self.banner()
        max_pages = self.prompt('Enter max pages to crawl (e.g, 50, Default): ')
 
        if not max_pages:
            max_pages = 50
        
        elif not max_pages.isdigit():
            MsgDCR.FailureMessage('Please enter valid number')
            self.back2menu_prompt()
            self.change_settings()
        
        self.banner()
        zhe = self.prompt('Enter your ZHE (e.g, 098f6bcd4621d373cade4e832627b4f6): ')

        if not zhe:
            MsgDCR.FailureMessage('The ZHE is required for grabbing urls!')
            self.back2menu_prompt()
            self.change_settings()

        self.banner()
        phpsessid = self.prompt('Enter your PHPSESSID (e.g, ovfjv1un3ha1o470qj1a4u6hgv): ')
        
        if not phpsessid:
            MsgDCR.FailureMessage('The PHPSESSID is required for grabbing urls!')
            self.back2menu_prompt()
            self.change_settings()
        
        write_cfg(
            output_dir=output_dir,
            time_date=time_date,
            max_pages=int(max_pages),
            ZHE=zhe,
            PHPSESSID=phpsessid
        )

        self.banner()
        MsgDCR.SuccessMessage('Configurations successfully set')
        self.back2menu_prompt()
        return


    def grab_archives(self, file_name: str = None):
        self.banner()

        if not self.data:
            MsgDCR.FailureMessage('Some required settings are missing. Please set ZHE and PHPSESSID in the \'Settings\' menu.')
            self.back2menu_prompt()
            return
        
        if not file_name:
            file_name = self.prompt('Enter your file name (e,g. Alex): ')
        file_name = f'{self.output_dir}{file_name}{(self.time_now() if self.time_date else "")}.txt'
        self.banner()
        MsgDCR.InfoMessage(f'The extracted URLs will be saved into {file_name}')
        time.sleep(2)
        self.banner()

        for pages in range(self.config['max_pages']):
            self.request_zone(
                file_name=file_name, 
                url=f'http://www.zone-h.org/archive/page={pages}', 
                pages=pages, 
                shown_name='Archive'
            )
        self.back2menu_prompt()

    def grab_specials(self, file_name: str = None):
        self.banner()

        if not self.data:
            MsgDCR.FailureMessage('Some required settings are missing. Please set ZHE and PHPSESSID in the \'Settings\' menu.')
            self.back2menu_prompt()
            return

        if not file_name:
            file_name = self.prompt('Enter your file name (e,g. Alex): ')
        file_name = f'{self.output_dir}{file_name}{(self.time_now() if self.time_date else "")}.txt'
        self.banner()
        MsgDCR.InfoMessage(f'The extracted URLs will be saved into {file_name}')
        time.sleep(2)
        self.banner()

        for pages in range(self.config['max_pages']):
            self.request_zone(
                file_name=file_name, 
                url=f'http://www.zone-h.org/archive/special=1/page={pages}', 
                pages=pages, 
                shown_name='Special'
            )
        self.back2menu_prompt()

    def grab_onholds(self, file_name: str = None):
        self.banner()
        
        if not self.data:
            MsgDCR.FailureMessage('Some required settings are missing. Please set ZHE and PHPSESSID in the \'Settings\' menu.')
            self.back2menu_prompt()
            return
        
        if not file_name:
            file_name = self.prompt('Enter your file name (e,g. Alex): ')
        file_name = f'{self.output_dir}{file_name}{(self.time_now() if self.time_date else "")}.txt'
        self.banner()
        MsgDCR.InfoMessage(f'The extracted URLs will be saved into {file_name}')
        time.sleep(2)
        self.banner()

        for pages in range(self.config['max_pages']):
            self.request_zone(
                file_name=file_name, 
                url=f'http://www.zone-h.org/archive/published=0/page={pages}', 
                pages=pages, 
                shown_name='OnHold'
            )

        self.back2menu_prompt()
    
    def grab_notifier(self, notifier: str = None):
        self.banner()
        
        if not self.data:
            MsgDCR.FailureMessage('Some required settings are missing. Please set ZHE and PHPSESSID in the \'Settings\' menu.')
            self.back2menu_prompt()
            return
        
        if not notifier:
            notifier = self.prompt('Enter your Notifier name (e,g. Mr.ROBOT): ')
        notifier = f'{self.output_dir}{notifier}{(self.time_now() if self.time_date else "")}.txt'
        self.banner()
        MsgDCR.InfoMessage(f'The extracted URLs will be saved into {notifier}')
        time.sleep(2)
        self.banner()

        for pages in range(self.config['max_pages']):
            self.request_zone(
                file_name=notifier, 
                url=f'http://www.zone-h.org/archive/notifier={notifier}/page={pages}', 
                pages=pages, 
                shown_name='Notifier'
            )
        self.back2menu_prompt()


if __name__ == '__main__':
    app = ChZoneGrabber()
    app.run()

