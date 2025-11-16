# -*- coding: utf-8 -*-
# core/config_parser.py

import os
import sys
import configparser

from core.config import Config
from ui.decorators import MsgDCR

def read_cfg():
    """Read and parse a CFG file."""
    if not os.path.exists(Config._config_file):
        MsgDCR.FailureMessage(f"Configuration file '{Config._config_file}' not found.")
        sys.exit(2)

    config = configparser.ConfigParser()
    config.read(Config._config_file)

    try:
        output_dir = config.get('CONFIG', 'output_dir', fallback='reports/')
        time_date = config.getboolean('CONFIG', 'time_date', fallback=True)
        max_pages = config.getint('CONFIG', 'max_pages', fallback=50)
        ZHE_cookie = config.get('ZONE-H CONFIG', 'ZHE', fallback=None)
        PHPSESSID_cookie = config.get('ZONE-H CONFIG', 'PHPSESSID', fallback=None)
    except Exception:
        MsgDCR.FailureMessage('Error on accessing config values')
        sys.exit(2)
    
    return {
        'output_dir': output_dir,
        'time_date': time_date,
        'max_pages': max_pages,
        'ZHE': ZHE_cookie,
        'PHPSESSID': PHPSESSID_cookie
    }

def write_cfg(output_dir: str = 'reports/', time_date: bool = True, max_pages: int = 50, ZHE: str = '', PHPSESSID: str = ''):
    """Create or update a CFG file."""
    _configs = '[CONFIG]\n'
    _configs += ' # The output files are placed inside this directory.\n'
    _configs += f'output_dir = {output_dir}\n'
    _configs += ' # The time and date are added after the name of each file.\n'
    _configs += f'time_date = {time_date}\n'
    _configs += '# maximum number of pages for crawling\n'
    _configs += f'max_pages = {max_pages}\n\n\n'
    _configs += '# You definitely need to define these two variables in order to be able to do this.\n'
    _configs += '# Read the project\'s documentation file: "README.md" \n'
    _configs += '# Or\n'
    _configs += '# visit this page: https://github.com/Ch4120N/ChZoneGrabber\n'
    _configs += '[ZONE-H CONFIG]\n'
    _configs += f'ZHE = {ZHE}\n'
    _configs += f'PHPSESSID = {PHPSESSID}\n'

    with open(Config._config_file, "w") as config_file:
        config_file.write(_configs)