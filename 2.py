#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 12:44:37 2017

@author: malcolm
"""
import collections
import re

raw = open('2_input.txt').read().lower()

charraw = re.findall('.?', raw)

cnt = collections.Counter(charraw)

charfilt = re.findall('[aeilqtuy]', raw)

print(charfilt)