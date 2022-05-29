#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 13:46:23 2022

@author: robertocappiello
"""

class FinancialAccount:
  def __init__(self, amount):
    self.account = amount
    
  def __eq__(self, other):
    return self.account == other.account
    
class BankAccount(FinancialAccount):
  pass

class InvestmentAccount(FinancialAccount):
  pass

my_banking = BankAccount(500)
my_investments = InvestmentAccount(750)
print(my_investments == my_banking)

class FinancialAccount:
  def __init__(self, amount):
    self.account = amount
    
  def __truediv__(self, other):
    return self.account / other.account
    
class BankAccount(FinancialAccount):
  pass

class InvestmentAccount(FinancialAccount):
  pass

my_banking = BankAccount(500)
my_investments = InvestmentAccount(750)
print(my_investments / my_banking)

class FinancialAccount:
  def __init__(self, amount):
    self.account = amount
    
  def __floordiv__(self, other):
    return self.account // other.account
    
class BankAccount(FinancialAccount):
  pass

class InvestmentAccount(FinancialAccount):
  pass

my_banking = BankAccount(500)
my_investments = InvestmentAccount(750)
print(my_investments // my_banking)