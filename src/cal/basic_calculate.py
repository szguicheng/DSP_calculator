#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\Guicheng\Desktop\Hello World\DSP_calculator\src\cal\material_cal.py
# Project: c:\Users\Guicheng\Desktop\Hello World\DSP_calculator\src\cal
# Created Date: Saturday, November 30th 2024, 1:11:07 am
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
# 2024-11-30	GC	basic calculate finished(need to add document)
###

from src.locate_item import Locatorfname, Locatorfid
from src.joinpath import joinpath as jp
import json


class Calculator:

    def __init__(self, name: str = None, id: int = None):
        """
        given the ``name`` or ``id`` of the item, calculate the data needed.
        """
        if name is None and id is None:
            raise ValueError("Either ``name`` or ``id`` must be provided.")
        if name is not None:
            self.id = Locatorfname().id(name)
            self.name = name
        if id is not None:
            self.name = Locatorfid().name(id)
            self.id = id
        with open(jp("src/data/item.json"), 'r', encoding='utf-8') as a:
            self.im = json.load(a)
        with open(jp("src/data/recipes.json"), 'r', encoding='utf-8') as b:
            self.rp = json.load(b)

    def need(self, num: int) -> tuple:
        """
        Find the recipe by the id of the product.

        :param id: The id of the product.
        :type id: int

        :return: A tuple containing multiple dictionaries with the recipe details of the product.

            - ``items`` (*tuple*): A tuple containing the IDs of the items (int).
            - ``itemCounts`` (*tuple*): A tuple containing the quantity needed for each item.
            - ``results`` (*tuple*): A tuple containing the IDs of the products (int).
            - ``resultCounts`` (*tuple*): A tuple containing the quantity of the products (int).
            - ``timeSpend`` (*int*): The time needed to produce the items.
            - ``manuType`` (*str*): The type of the production method.

        :rtype: tuple

        :raise KeyError: If the item with the specified id is not found.

        :Example:
        >>> print(Calculator("有机晶体").need(2))
        [{'items': [1115,1114,1000], "itemCounts": [2,1,1], "results":[1117],"resultCounts":[1], 'timeSpend': 360, 'manuType': "CHEMICAL'},{}]
        """
        method_id = []
        for item in self.rp:
            if self.id in item['results']:
                method_id.append(item['id'])
        method_num = len(method_id)
        need_dict = []
        for i in range(method_num):
            for xx in self.rp:
                if method_id[i] == xx['id']:
                    items = xx['items']
                    itemCounts = xx['itemCounts']
                    results = xx['results']
                    resultCounts = xx['resultCounts']
                    timeSpend = xx['timeSpend']
                    manuType = xx['type']

                    productCount = [
                        count for x, count in zip(results, resultCounts)
                        if x == self.id
                    ][0]
                    extraProduct = [
                        x for x, count in zip(results, resultCounts)
                        if x != self.id
                    ]
                    extraCount = [(count / productCount * num)
                                  for x, count in zip(results, resultCounts)
                                  if x != self.id]
                    itemCounts = [(x / productCount * num) for x in itemCounts]
                    resultCounts = [(x / productCount * num)
                                    for x in resultCounts]
                    timeSpend = timeSpend / productCount * num
                    need_dict.append({
                        'items': items,
                        'itemCounts': itemCounts,
                        'results': results,
                        'resultCounts': resultCounts,
                        'timeSpend': timeSpend,
                        'manuType': manuType,
                        'extraProduct': extraProduct,
                        'extraCount': extraCount
                    })
        return need_dict


if __name__ == '__main__':
    cal = Calculator(name="精炼油")
    print(cal.need(4))
