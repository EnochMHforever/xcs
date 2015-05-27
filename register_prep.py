#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Prepares for registration.
__author__ = 'Aaron Hosford'

import glob
import os

from xcs import __version__
import build_readme

build_readme.build_readme()
os.system('python setup.py sdist bdist_wheel')

with open('xcs.egg-info/PKG-INFO', encoding='utf-8', mode='rU') as infile:
    with open('xcs.egg-info/PKG-INFO-FIXED', encoding='utf-8', mode='w') as outfile:
        prev_skipped = False
        for line in infile:
            if line.strip() or prev_skipped:
                outfile.write(line)
                prev_skipped = False
            else:
                prev_skipped = True
os.remove('xcs.egg-info/PKG-INFO')
os.rename('xcs.egg-info/PKG-INFO-FIXED', 'xcs.egg-info/PKG-INFO')

dist = glob.glob('dist\\*' + __version__ + '*.whl')[-1]
print(dist)
os.system('pip install dist\\' + os.path.basename(dist) + ' --upgrade')


