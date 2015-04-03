# -*- coding: utf-8 -*-

'''
Created on 03.04.2015

@author: christopher
'''

class Player:
    def __init__(self, inputName):
        self.name = inputName
        self.cards = []
        
    def showCards(self):
        for i in range(len(self.cards)):
            print self.cards[i].color, self.cards[i].value
    