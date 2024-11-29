#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\Guicheng\Desktop\Hello World\DSP_calculator\src\joinpath.py
# Project: c:\Users\Guicheng\Desktop\Hello World\DSP_calculator\src
# Created Date: Friday, November 29th 2024, 1:04:29 pm
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


import os

def joinpath(path: str) -> str:
    '''
    Join paths with the current directory.

    ``*paths``: One or more path fragments.

    Returns:
    str: The joined full path.

    Example:
    >>> joinpath("folder", "subfolder", "file.txt")
    'current_directory/folder/subfolder/file.txt'
    '''
    current_dir = os.path.dirname(__file__)
    project_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
    path = os.path.normpath(path)
    full_path = os.path.join(project_dir, path)
    return os.path.normpath(full_path)
