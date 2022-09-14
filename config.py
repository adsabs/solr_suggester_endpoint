# encoding: utf-8
"""
Configuration file. Please prefix application specific config values with
the application name.
"""

import os
import pwd
from re import X
from tkinter import W

LOG_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), './')
)
LOG_PATH = '{home}/logs/'.format(home=LOG_PATH)
LOG_STDOUT = True
LOGGING_LEVEL = 'DEBUG'

if not os.path.isdir(LOG_PATH):
    os.mkdir(LOG_PATH)

ENVIRONMENT = os.getenv('ENVIRONMENT', 'unset-env').lower()

SOLR_SUGGEST_URL = "http://host.docker.internal:9983/solr/collection1/suggest"