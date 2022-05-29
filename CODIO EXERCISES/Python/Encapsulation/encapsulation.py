#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 12:27:11 2022

@author: robertocappiello
"""

class Phone:
  def __init__(self, make, storage, megapixels):
    self.make = make
    self.storage = storage
    self.megapixels = megapixels
    
my_phone = Phone("iPhone", 256, 12)
print(my_phone.make)
print(my_phone.storage)
print(my_phone.megapixels)

my_phone = Phone("iPhone", 256, 12)
print(my_phone.storage)
my_phone.storage = 64
print(my_phone.storage)