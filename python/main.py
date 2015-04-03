# -*- coding: utf-8 -*-

'''
Created on 03.04.2015

@author: christopher
'''

from game import Game

class Main:
    def __init__(self):
        self.game = Game()
        self.game.createCards()
        self.game.shuffleCards()
        
        #self.showCards()
        
        self.game.addPlayer("Schleicher")
        self.game.addPlayer("Udo")
        self.game.addPlayer("Peetzweg")
        self.game.addPlayer("Commander")
        
        self.game.giveCards()
        #self.game.players[0].showCards()
    
    def showCards(self):
        for i in range(len(self.game.cards)):
            print self.game.cards[i].color, self.game.cards[i].value
        
if __name__ == "__main__":
    Main()
