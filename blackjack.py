# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 11:10:10 2021

@author: sree
"""

import random 

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
          'Queen':10, 'King':10, 'Ace':11}

class card:
    def __init__(self,suits,ranks):
        self.suits=suits
        self.ranks=ranks
        
    def __str__(self):
        return self.suits+'of'+self.ranks
    
class deck:
     def __init__(self):
         self.deck=[]
         for suit in suits:
           for rank in ranks:
             self.deck.append(card(suit, rank))
             
     def __str__(self):
          deck_comp =' '
          for card in self.deck:
              deck_comp +='\n'+card.__str__()
              return ' the deck has '+deck_comp
     def shuffle(self):
          random.suffle(self.deck)
     def deal(self):
         one_card =self.deck.pop()
         return one_card
class hand:
     
          def __init__(self):
              self.card=[]
              self.value= 0
              self.ace =0
          def add_Card(self,card):
             self.card.append(card)
             self.values+=values[card.rank]
  
class bet:
      def __init__(self):
           self.total_bet=100
           self.bet=0
           
      def win_bet(self):
           self.total+=self.bet 
           
      def lose_bet(self):
           self.total-=self.bet
           
           
def take_bet(chips):

    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed",chips.total)
            else:
                break
            
def hit(self, hand, deck):
     hand.add_card(card = deck.deal())
     hand.adjust_for_ace()
     
def hit_stand(self,hand):
    
    global playing 
    player_choice=input("hit or stand")
    
    while player_choice.lower() is not in ['hit' , 'stand']:
        player_choice=input("hit or stand")
        
    if player_choice is lower()=="hit"
       hit(deck,hand)
    else:
        print("player stands and dealer turns")
        playing=false
        
        
def show_all(player,dealer):
    print(Fore.GREEN + "********")
    print(Fore.RED + "Player card: {}".format(player.cards))
    print(Fore.RED + "Player sum of cards: {}".format(player.value))
    print(Fore.GREEN + "********")
    print(Fore.RED + 'Dealer cards: {}'.format(dealer.cards))
    print(Fore.RED + "Dealer sum of cards: {}".format(dealer.value))
    print(Fore.GREEN + "********")

def player_busts(player,chip):
    if player.values>21 
      print("player busted)  
    chip.lose_bet() 
    
def  player_wins(player,dealer,chip):
    if dealer.values<player.values<=21:
        print("player wins")
    chip.wins_bet()

def dealer_busts(dealer, chip):
    if dealer.values>21:
        print("dealer busts")
    chip.lose_bet()
    
def  dealer_wins(player,dealer,chip):
    if player.values<dealer.values<=21:
        print("dealer wins")
    chip.wins_bet()
    
def push(dealer,player):
    
    if dealer.values==player.values:
    print("both are equal so push")
    
    
print("Hello! Welcome to the Blackjack game!")
while True:
    while True:
            game = input("Are you ready to play? Yes/No: ")
            if game.lower() not in ["yes","no"]:
                continue
            else:
                break
            
 if game.lower() == "no":
        print("Goodbye :( ")
        break
    
 mydeck = Deck()
    mydeck.shuffle()
    
    player = Hand()
    dealer = Hand()
    
    player.add_card(card = mydeck.deal())
    dealer.add_card(card = mydeck.deal())
    
    player.add_card(card = mydeck.deal())
    dealer.add_card(card = mydeck.deal())
        
    # Set up the Player's chips
    mychip = Chips() 
    # Prompt the Player for their bet
    take_bet(mychip)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player,dealer)
    
    while playing:  # recall this variable from our hit_or_stand function
        # Prompt for Player to Hit or Stand
        hit_or_stand(mydeck,player)
        # Show cards (but keep one dealer card hidden)
        show_some(player,dealer)
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value >21:
            player_busts(player,mychip)
            break
        
if player.value > 21:
        pass
    else:
        dealerturn = dealer.value        
        while dealerturn <= 17:
            hit(mydeck,dealer)
            dealerturn = dealer.value  
    
    # Show all cards
    print("End of game:")    
    show_all(player,dealer)
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
           

    















           
          
          
    
            
             
    