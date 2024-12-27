############### Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


import random
#from art import logo
import os

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
  
def calculate_score(card):
  if sum(card) == 21 and len(card) == 2:
    print("It's a blackjack!")
    return 0
  elif sum(card) > 21 and 11 in card:
    card.remove(11)
    card.append(1)
  return sum(card)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "It's a draw"
  elif computer_score == 0:
    return "The user lost and dealer won"
  elif user_score == 0:
    return "The user win and dealer lost"
  elif user_score > 21:
    return "The user lost and dealer won"
  elif computer_score > 21:
    return "The computer lost and user won"
  elif user_score > computer_score:
    return "The user won and dealer lost"
  else:
    return "The user lost and dealer won"


def play_blackjack():
  
  user_card = []
  computer_card = []
  should_continue = True
  #print(logo)
  
  for i in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())
  
  while should_continue:
    user_score = calculate_score(card = user_card)
    computer_score = calculate_score(card = computer_card)
    print(f"The user has: {user_card}. The User's total score is: {user_score}. The computer shows: {computer_card[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      should_continue = False  
    else:
      new_card = input("Would you like another card? Type 'y' to hit, type 'n' to stand: ")
      if new_card == 'y':
        user_card.append(deal_card())
      else:
        should_continue = False
  
  while computer_score != 0 and computer_score < 17:
    computer_card.append(deal_card())
    computer_score = calculate_score(card = computer_card)
    print(f"The computer now has {computer_card}. The computer score is {calculate_score(computer_card)}")
    
  
  print(compare(user_score, computer_score))
  restart = input("Would you like to play again? Type 'yes' to continue or 'no' to quit: ")
  if restart == 'yes':
    os.system('cls' if os.name == 'nt' else 'clear')
    play_blackjack()
  else:
    print("Thank you for playing! ")

play_blackjack()
