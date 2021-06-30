#!/usr/bin/env python
# -*- encoding: utf-8 -*-
##
# Copyright 2017 FIWARE Foundation, e.V.
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
##

from configparser import ConfigParser
import logging
from os import environ
from os.path import dirname, join, abspath
from json import load

__author__ = 'Fernando López'

__version__ = '1.0.0'


"""
Default configuration.

The configuration `cfg_defaults` are loaded from `cfg_filename`, if file exists in
/etc/fiware.d/links.ini

Optionally, user can specify the file location manually using an Environment variable
called SELENIUM_CONF_FILE.
"""

name = 'links'

cfg_dir = "/etc/fiware.d"

cfg_filename = environ.get("SELENIUM_CONF_FILE")
if cfg_filename:
    cfg_dir = dirname(cfg_filename)
else:
    cfg_filename = join(cfg_dir, '%s.json' % name)

with open(cfg_filename) as f:
    LINKS = load(f)

CODE_HOME = dirname(dirname(abspath(__file__)))
LOG_HOME = join(CODE_HOME, 'logs')
DRIVER_HOME = join(CODE_HOME, 'drivers')
