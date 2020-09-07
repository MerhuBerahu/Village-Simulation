#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module's deals with the different types of shops
"""

class Base_shop():
    def __init__(self, shop_name, shop_hours, shop_type):
        self.shop_name = shop_name
        self.shop_hours = shop_hours
        self.shop_type = shop_type
