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

