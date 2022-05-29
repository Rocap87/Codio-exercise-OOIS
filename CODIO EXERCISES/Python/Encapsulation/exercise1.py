#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 13:12:47 2022

@author: robertocappiello
"""

class Country:
    def __init__(self, name, capital, population, continent):
        self._name = name
        self._capital = capital
        self._population = population
        self._continent = continent

my_country = Country("France", "Paris", 67081000, "Europe")
print(my_country._name)
print(my_country._capital)
print(my_country._population)
print(my_country._continent)