#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 12:43:41 2022

@author: robertocappiello
"""

import csv

# **********************************************
# code for the coffee object
# **********************************************
class CoffeeJournal:
  def __init__(self, file):
    self._file = file
    self._roaster = ""
    self._country = ""
    self._region = ""
    self._stars = ""
    self._new_coffee = []
    self._old_coffee = self.load_coffee()

  def load_coffee(self):
    coffee = []
    with open(self._file) as f:
      reader = csv.reader(f, delimiter=',')
      for row in reader:
        coffee.append(row)
    return coffee

# **********************************************
# code for testing your script
# **********************************************

test_object = CoffeeJournal("code/encapsulation/test_journal1.csv")
test_object.load_coffee()
print(test_object._old_coffee)