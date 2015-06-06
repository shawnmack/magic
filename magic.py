import random
import json

#example of a list


class Driver(object):

    def __init__(self,):
        turn=0
        p1roll=random.randrange(0, 7)+random.randrange(0, 7)
        p2roll=random.randrange(0, 7)+random.randrange(0, 7)
        print('You roll', p1roll, 'and they roll', p2roll, '.')
        if p1roll>p2roll:
            print('You go first.')
        else:
            print('You are on the draw.')
            turn=1

            
class Game(object):

    def __init__(self,turn):
        if turn==1:
class Card(object):

    def set_mana(self, x):
        self.mana = x
    def get_mana(self):
          return self.mana

    def __init__(self,manacost):
         self.set_mana(manacost)
         
         

class Player(object):

      def __init__(self, title,deck):
         self.myDeck=deck
         self.name=title
         life=20
         wins=0
         loss=0

class Land(Card):
    
    def set_mana(self, x):
        self.mana = x
    def get_mana(self):
          return self.mana

    def __init__(self, type):
         self.name=type
         self.mana=0

class Permanent(Card):

    def set_mana(self, x):
        self.mana = x
    def get_mana(self):
          return self.mana

    def __init__(self, type, manacost):
         self.name=type
         self.set_mana(manacost)
         
class Instant(Card):

    def set_mana(self, x):
        self.mana = x
    def get_mana(self):
          return self.mana

    def __init__(self, type, manacost):
         self.name=type
         self.set_mana(manacost)

class Sorcery(Card):
   
    def set_mana(self, x):
        self.mana = x
    def get_mana(self):
          return self.mana
    def __init__(self, type, manacost):
         self.name=type
         self.set_mana(manacost)



 
driver=Driver()
    
