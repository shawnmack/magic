#This is a work in progress Magic the Gathering Emulator. Using card data in a data structure I will
#create an emulator and magic computer game.
import random
import csv
import sys
import datetime
import string

#
#
#
#
#MAGICAL EMULATOR
#
#Shawn Mack 2015
#


#
#SOURCE
#

#Module to import data 
def card_import(file_name):
    f = open(file_name,'rb')
 

         print('Success',' at', datetime.datetime.now())
         f.close()

#Initiates a game with an opponent
class Driver(object):


 
    #Constructor
    def __init__(self):


        #calling to import card data
        card_import('magic.csv')

        print(datetime.datetime.now())
        turn=0
        p1roll=random.randrange(0, 7)+random.randrange(0, 7)
        p2roll=random.randrange(0, 7)+random.randrange(0, 7)
        print('You roll', p1roll, 'and they roll', p2roll, '.')
        if p1roll>p2roll:
            print('You go first.')
        else:
            print('You are on the draw.')
            turn=1



#Card master object     
class Card(object):

    def set_mana(self, x):
        self.mana = x
    def get_mana(self):
          return self.mana
    def __init__(self,manacost):
         self.set_mana(manacost)
         
         
#Player
class Player(object):

      def __init__(self, title,deck):
         self.myDeck=deck
         self.name=title
         life=20
         wins=0
         loss=0

#Land
class Land(Card):
    
    def set_mana(self, x):
        self.mana = x
    def get_mana(self):
          return self.mana

    def __init__(self, type):
         self.name=type
         self.mana=0

#Permanent
class Permanent(Card):

    def set_mana(self, x):
        self.mana = x
    def get_mana(self):
          return self.mana

    def __init__(self, type, manacost):
         self.name=type
         self.set_mana(manacost)

#Instant         
class Instant(Card):

    def set_mana(self, x):
        self.mana = x
    def get_mana(self):
          return self.mana

    def __init__(self, type, manacost):
         self.name=type
         self.set_mana(manacost)
#Sorcery
class Sorcery(Card):
   
    def set_mana(self, x):
        self.mana = x
    def get_mana(self):
          return self.mana
    def __init__(self, type, manacost):
         self.name=type
         self.set_mana(manacost)


#
#DRIVER
#
 
driver=Driver()
