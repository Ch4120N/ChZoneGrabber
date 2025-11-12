# -*- coding: utf-8 -*-
# core/banner.py

from colorama import Fore, init
init(autoreset=True)


def Banner():
    return fr'''
{Fore.LIGHTRED_EX}    ___ _     _____                   ___           _     _               
{Fore.LIGHTRED_EX}   / __\ |__ / _  / ___  _ __   ___  / _ \_ __ __ _| |__ | |__   ___ _ __ 
{Fore.LIGHTRED_EX}  / /  | '_ \\// / / _ \| '_ \ / _ \/ /_\/ '__/ _` | '_ \| '_ \ / _ \ '__|
{Fore.LIGHTRED_EX} / /___| | | |/ //\ (_) | | | |  __/ /_\\| | | (_| | |_) | |_) |  __/ |   
{Fore.LIGHTRED_EX} \____/|_| |_/____/\___/|_| |_|\___\____/|_|  \__,_|_.__/|_.__/ \___|_|
{Fore.LIGHTRED_EX} 
{Fore.LIGHTRED_EX}                         {Fore.LIGHTWHITE_EX}Owned By {Fore.LIGHTBLUE_EX}[ {Fore.LIGHTRED_EX}Ch4120N {Fore.LIGHTBLUE_EX}]
{Fore.LIGHTRED_EX}           {Fore.LIGHTWHITE_EX}GitHub: {Fore.LIGHTGREEN_EX}https://github.com/Ch4120N/ChZoneGrabber
{Fore.RESET}'''

