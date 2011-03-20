#!/usr/bin/env python

"""
Passenger WSGI script for hosting on Dreamhost. Assumes a virtualenv
configured at ~/env/[appname].
"""

import sys
import os

INTERP = os.path.expanduser("~/env/[appname]/bin/python")
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(os.getcwd())

from [appname] import app as application
