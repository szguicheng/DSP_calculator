#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\Guicheng\Desktop\Hello World\DSP_calculator\src\locate_item.py
# Project: c:\Users\Guicheng\Desktop\Hello World\DSP_calculator\src
# Created Date: Friday, November 29th 2024, 7:34:38 pm
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
###

import json
from joinpath import joinpath as jp

class Locatorfname:
    def __init__(self):
        json_path = jp("src/data/item.json")
        with open(json_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def id(self, name: str) -> int:
        """
        Find the id of the item by the name.

        Parameters:
        name (str): The name of the item.

        Returns:
        int: The id of the item.

        Raises:
        KeyError: If the item with the specified name is not found.

        Example:
        >>> find_id("item_name")
        1001
        """
        for item in self.data:
            if item['name'] == name:
                return item['id']
        raise KeyError(f"Item {name} not found.")

    def type(self, name: str) -> str:
        """
        Find the type of the item by the name.

        Parameters:
        name (str): The name of the item.

        Returns:
        str: The type of the item.

        Raises:
        KeyError: If the item with the specified name is not found.

        Example:
        >>> find_type("item_name")
        "RESOURCE"
        """
        for item in self.data:
            if item['name'] == name:
                return item['type']
        raise KeyError(f"Item {name} not found.")
    
    def icon(self, name: str) -> str:
        """
        Find the icon path of the item by the name.

        Parameters:
        name (str): The name of the item.

        Returns:
        str: The icon path of the item.

        Raises:
        KeyError: If the item with the specified name is not found.

        Example:
        >>> find_icon("item_name")
        "Icons/ItemRecipe/iron-ore"
        """
        for item in self.data:
            if item['name'] == name:
                return item['iconPath']
        raise KeyError(f"Item {name} not found.")
    
    def description(self, name: str) -> str:
        """
        Find the description of the item by the name.

        Parameters:
        name (str): The name of the item.

        Returns:
        str: The description of the item.

        Raises:
        KeyError: If the item with the specified name is not found.

        Example:
        >>> find_description("item_name")
        "A piece of iron ore."
        """
        for item in self.data:
            if item['name'] == name:
                return item['description']
        raise KeyError(f"Item {name} not found.")
    
class Locatorfid:
    def __init__(self):
        json_path = jp("src/data/item.json")
        with open(json_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
    def name(self, id: int) -> str:
        """
        Find the name of the item by the id.

        Parameters:
        id (int): The id of the item.

        Returns:
        str: The name of the item.

        Raises:
        KeyError: If the item with the specified id is not found.

        Example:
        >>> find_name(1001)
        "iron-ore"
        """
        for item in self.data:
            if item['id'] == id:
                return item['name']
        raise KeyError(f"Item {id} not found.")
    
    def type(self, id: int) -> str:
        """
        Find the type of the item by the id.

        Parameters:
        id (int): The id of the item.

        Returns:
        str: The type of the item.

        Raises:
        KeyError: If the item with the specified id is not found.

        Example:
        >>> find_type(1001)
        "RESOURCE"
        """
        for item in self.data:
            if item['id'] == id:
                return item['type']
        raise KeyError(f"Item {id} not found.")
    
    def icon(self, id: int) -> str:
        """
        Find the icon path of the item by the id.

        Parameters:
        id (int): The id of the item.

        Returns:
        str: The icon path of the item.

        Raises:
        KeyError: If the item with the specified id is not found.

        Example:
        >>> find_icon(1001)
        "Icons/ItemRecipe/iron-ore"
        """
        for item in self.data:
            if item['id'] == id:
                return item['iconPath']
        raise KeyError(f"Item {id} not found.")
    
    def description(self, id: int) -> str:
        """
        Find the description of the item by the id.

        Parameters:
        id (int): The id of the item.

        Returns:
        str: The description of the item.

        Raises:
        KeyError: If the item with the specified id is not found.

        Example:
        >>> find_description(1001)
        "A piece of iron ore."
        """
        for item in self.data:
            if item['id'] == id:
                return item['description']
        raise KeyError(f"Item {id} not found.")