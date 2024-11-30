#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\Guicheng\Desktop\Hello World\DSP_calculator\src\locate_recipes.py
# Project: c:\Users\Guicheng\Desktop\Hello World\DSP_calculator\src
# Created Date: Saturday, November 30th 2024, 1:56:38 am
# Author: GUI Cheng
# -----
# Last Modified: Sat Nov 30 2024
# Modified By: GUI Cheng
# -----
# It's a great pelasure to have the life running on the world.
# Be patient and kind to yourself.
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	----------------------------------------------------------
# 2024-11-30	GC	Please not use this file, it's not finished yet.
###


import json
from src.joinpath import joinpath as jp
from src.locate_item import Locatorfname, Locatorfid

class Locaterecipe:
    def __init__(self):
        with open(jp("src/data/recipes.json"), 'r', encoding='utf-8') as a:
            self.rp = json.load(a)
        with open(jp("src/data/item.json"), 'r', encoding='utf-8') as b:
            self.im = json.load(b)
    
    def fname(self, name:str) -> dict:
        """
        Find the recipe by the name of the product.

        :param name: The name of the product.
        :type name: str

        :return: A dictionary containing the recipe of the product.
            - ``items``: a tuple containing the id of the item.
            - ``itemCounts``: a tuple containing the need of the item.
            - ``resultCounts``: the number of the product(int).
            - ``timeSpend``: the time needed to produce the item(int).
            - ``manuType``: the type of the production method.
            - ``rawName``: a tuple containing the Chinese name of the item.
        :rtype: dict

        :raise KeyError: If the item with the specified name is not found.

        :Example:
        >>> find_recipe("磁线圈")
        {'item_id': [1102, 1104], "itemCounts": [2,1], 'timespend': 60, 'rawName': ['磁铁','铜块']}
        """
        for item in self.rp:
            if item['name'] == name:
                items = item['items']
                itemCounts = item['itemCounts']
                resultCounts = item['resultCounts']
                timeSpend = item['timeSpend']
                manuType = item['type']
                rawName = []
                for i in items:
                    rawName.append(Locatorfid().name(i))
                return {'items': items, "itemCounts": itemCounts, "resultCounts": resultCounts,'timeSpend': timeSpend, 'manuType':manuType,'rawName': rawName}
        raise KeyError(f"Item {name} not found.")

    def fid(self, id:int) -> dict:
        """
        Find the recipe by the id of the product.

        :param id: The id of the product.
        :type id: int

        :return: A dictionary containing the recipe of the product.
            - ``items``: a tuple containing the id of the item.
            - ``itemCounts``: a tuple containing the need of the item.
            - ``resultCounts``: the number of the product(int).
            - ``timeSpend``: the time needed to produce the item(int).
            - ``manuType``: the type of the production method.
            - ``rawName``: a tuple containing the Chinese name of the item.
        :rtype: dict

        :raise KeyError: If the item with the specified id is not found.

        :Example:
        >>> find_recipe(1102)
        {'items': [1102, 1104], "itemCounts": [2,1], "resultCounts":[1], 'timespend': 60, 'manuType': "ASSEMBLE', 'rawName': ['磁铁','铜块']}
        """
        id = str(id)
        for item in self.rp:
            if item['sid'] == id:
                items = item['items']
                itemCounts = item['itemCounts']
                resultCounts = item['resultCounts']
                timeSpend = item['timeSpend']
                manuType = item['type']
                rawName = []
                for i in items:
                    rawName.append(Locatorfid().name(i))
                return {'items': items, "itemCounts": itemCounts, "resultCounts": resultCounts,'timeSpend': timeSpend, 'manuType':manuType,'rawName': rawName}
        raise KeyError(f"Item {id} not found.")
    
