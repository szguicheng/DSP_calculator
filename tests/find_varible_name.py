#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\Guicheng\Desktop\Hello World\DSP_calculator\tests\find_varible.py
# Project: c:\Users\Guicheng\Desktop\Hello World\DSP_calculator\tests
# Created Date: Friday, November 29th 2024, 7:25:54 pm
# Author: GUI Cheng
# -----
# Last Modified: Fri Nov 29 2024
# Modified By: GUI Cheng
# -----
# It's a great pelasure to have the life running on the world.
# Be patient and kind to yourself.
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	----------------------------------------------------------
###


import json
import os
from src.joinpath import joinpath as jp

json_path = 'C:\\Users\\Guicheng\\Desktop\\Hello World\\DSP_calculator\\src\\data\\item.json'
type_list = []
with open(json_path,'r',encoding='utf-8') as f:
    data = json.load(f)
for i in data:
    type_list.append(i['type'])
print(set(type_list))