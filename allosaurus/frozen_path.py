# -*- coding: UTF-8 -*-

import sys
from os import path

def app_path():
    if hasattr(sys, 'frozen'):
        # we are running in a bundle
        frozen = 'ever so'
        return path.dirname(sys.executable)
    else:
        # we are running in a normal Python environment
        return path.dirname(__file__)