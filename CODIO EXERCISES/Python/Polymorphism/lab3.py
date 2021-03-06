#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 13:58:45 2022

@author: robertocappiello
"""

class Contacts:
  def __init__(self):
    self.view = 'list'
    self.contact_list = []
    self.choice = None
    self.index = None

  def display(self):
    while True:
      if self.view == 'list':
        self.show_list()
      elif self.view == 'info':
        self.show_info()
      elif self.view == 'add':
        print()
        self.add_contact()
      elif self.view == 'quit':
        print('\nClosing the contact list...\n')
        break
    
  def show_list(self):
    print()
    if len(self.contact_list) == 0:
        self.choice = input('(A)dd a new contact \n(Q)uit \n> ').lower()
    else:
        for index, contact in enumerate(self.contact_list):
            print(f"{index+1}) {contact.first_name} {contact.last_name}")
        self.choice = input('\n(#) Select a name \n(A)dd a new contact\n(Q)uit \n> ').lower() 
    self.handle_choice()

  def show_info(self):
    pass

  def __add__(self, new_contact):
    self.contact_list.append(new_contact)

  def add_contact(self):
    self + Information()
    self.view = 'list'

  def handle_choice(self):
      if self.choice == 'q':
          self.view = 'quit'
      elif self.choice == 'a' and self.view == 'list':
          self.view = 'add'
      elif self.choice.isnumeric() and self.view == 'list':
          index = int(self.choice) - 1
          if index >=0 and index < len(self.contact_list):
              self.index = index
              self.view = 'info'
  
class Information:
    def __init__(self):
        self.first_name = input('Enter first name: ')
        self.last_name = input('Enter last name: ')
        self.personal_phone = input('Enter personal phone number: ')
        self.personal_email = input('Enter personal email address: ')
        self.work_phone = input('Enter work phone number: ')
        self.work_email = input('Enter work email address: ')
        self.title = input('Enter work title: ')

contacts = Contacts()
contacts.display()