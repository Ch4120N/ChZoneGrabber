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
import argparse
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

from ui.banner import Banner
from ui.decorators import MsgDCR



class ChZoneGrabber:
    def __init__(self):
        pass

    def run(self):
        pass