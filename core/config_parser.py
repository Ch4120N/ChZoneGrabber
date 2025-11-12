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
        ZHE_cookie = config.get('ZONE-H CONFIG', 'ZHE', fallback='')
        PHPSESSID_cookie = config.get('ZONE-H CONFIG', 'PHPSESSID', fallback='')
    except Exception:
        MsgDCR.FailureMessage('Error on accessing config values')
        sys.exit(2)
    
    return {
        'output_dir': output_dir,
        'time_date': time_date,
        'ZHE': ZHE_cookie,
        'PHPSESSID': PHPSESSID_cookie
    }

def write_cfg():
    """Create or update a CFG file."""
    _configs = '[CONFIG]\n'
    _configs += 'output_dir = reports/ # The output files are placed inside this directory.\n'
    _configs += 'time_date = true # The time and date are added after the name of each file.\n\n\n'
    _configs += '# You definitely need to define these two variables in order to be able to do this.\n'
    _configs += '# Read the project\'s documentation file: "README.md" \n'
    _configs += '# Or\n'
    _configs += '# visit this page: https://github.com/Ch4120N/ChZoneGrabber\n'
    _configs += '[ZONE-H CONFIG]\n'
    _configs += 'ZHE = \n'
    _configs += 'PHPSESSID = \n'

    with open(Config._config_file, "w") as config_file:
        config_file.write(_configs)