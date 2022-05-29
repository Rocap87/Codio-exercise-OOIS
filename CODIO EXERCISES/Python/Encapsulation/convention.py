#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 12:28:24 2022

@author: robertocappiello
"""

class Phone:
  def __init__(self, model, storage, megapixels):
    self._model = model
    self._storage = storage
    self._megapixels = megapixels
class Phone:
  def __init__(self, model, storage, megapixels):
    self._model = model
    self._storage = storage
    self._megapixels = megapixels
    
my_phone = Phone("iPhone", 256, 12)
print(my_phone.__dict__)

class Phone:
  def __init__(self, model, storage, megapixels, carrier):
    self._model = model
    self._storage = storage
    self._megapixels = megapixels
    self._carrier = carrier
    
my_phone = Phone("iPhone", 256, 12, "AT&T")
print(my_phone.__dict__)

class PrivateClass:
  def __init__(self):
    self._private_attribute = "I am a private attribute"
  
  def _private_method(self):
    return "I am a private method"
    
obj = PrivateClass()
print(obj._private_method())