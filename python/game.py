# -*- coding: utf-8 -*-

'''
Created on 03.04.2015

@author: christopher
'''

from random import shuffle

from card import Card
from constants import Colors, Values
from player import Player

class Game:
    def __init__(self):
        self.cards = []
        self.players = []
        
    def createCards(self):
        for i in range(4):
            for j in range(5):
                for k in range(2):
                    self.cards.append(Card(Colors[i], Values[j]))
                    
    def shuffleCards(self):
        shuffle(self.cards)
        
    def giveCards(self):
        for i in range(len(self.cards) / 4):
            for j in range(len(self.players)):
                self.players[j].cards.append(self.cards[i+j])
        
    def addPlayer(self, name):
        self.players.append(Player(name))
