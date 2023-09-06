import random #Imports random module 

# Initialize deck
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades'] #Creates list of possible suits in the game
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace'] #Creates a list of ranks in the game
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11} #Creates a dictionary of values and assigns a written and numerical value to them

# Functions
def deal_card():    #Creates a function that deals card
    suit = random.choice(suits) #Takes a random choice from suits and assigns it to variable suit
    rank = random.choice(ranks) #Takes a random choice from ranks and assigns it to variable rank
    return (rank, suit) #Returns random choices that are assigned to rank and suit

def calculate_hand_value(hand): #Creates a function that calculates the hand value with input of hand
    value = sum([values[card[0]] for card in hand]) #Takes the value by taking the sum of the values of the hand that the user has
    num_aces = sum([1 for card in hand if card[0] == 'Ace']) #Takes the number of aces by summing every iteration where the ace is in the the user's hand
    
    while value > 21 and num_aces: #While the sum value of the hand is greater than 21 and number of aces exists...
        value -= 10 #Subtracts ten from the current value of the hand
        num_aces -= 1 #Subtracts one from the number of aces in the hand
    
    return value    #Returns the updated value of the hand

# Game setup
player_hand = [deal_card(), deal_card()] #Calls the variable that deals the card and saves it in a variable as the player's hand
dealer_hand = [deal_card(), deal_card()] #Calls the variable that deals the card and saves it in a variable as the dealer's hand

# Game loop
while True: #While loop that continuously ruins
    player_value = calculate_hand_value(player_hand)   #Takes the value of the player's hands by putting it into the function that calculates the hand's value
    dealer_value = calculate_hand_value(dealer_hand)    #Takes the value of the dealer's hands by putting it into the function that calculates the hand's value
    
    print("\nYour hand:", player_hand, "Value:", player_value) #Tells the user the hand they were given and the value of that hand
    print("Dealer's hand:", [dealer_hand[0], 'Hidden'])     #Prints the dealer's hand, but hides the value of the dealer's hand
    
    if player_value == 21:  #If the value of the player's hand is exactly 21
        print("Blackjack! You win!")    #Prints blackjack and the player won
        break    #Breaks the while loop 
    elif player_value > 21: #If the value of the player's hand is greater than 21
        print("Bust! You lose.")    #Prints that the player lost
        break   #Breaks the while loop
    
    action = input("Do you want to 'hit' or 'stand'? ").lower() #Asks the player if they want to hit or stand and saves their input as a variable called action
    
    if action == 'hit':    #If the user chooses hit...
        player_hand.append(deal_card()) #Calls the function that deals the card and adds it to the player's current hand
    elif action == 'stand': #Otherwise user chooses stand...
        while dealer_value < 17:   #While loop that happens when the value of the dealer's hand is less than 17...
            dealer_hand.append(deal_card()) #Calls the function that deals the card and adds it to the player's current hand
            dealer_value = calculate_hand_value(dealer_hand) #Calculates the value of the dealer's hand and saves it to variable dealer_value
        
        print("Dealer's hand:", dealer_hand, "Value:", dealer_value)   #Prints the hand and value of the dealer's hand
        
        if dealer_value > 21 or player_value > dealer_value:   #If either the dealer's hand value is greater than 21 or the value of the player's hands is greater than that of the dealer...
            print("You win!")   #Tells the user they won
        elif dealer_value > player_value:   #Otherwise the value of the dealer's hand is greater than the hand of the player...
            print("Dealer wins.")   #Tells the user the dealer won
        else:   #Otherwise - they tie...
            print("It's a tie!")    #Tells the user it was a tie
        
        break   #Breaks the while loop and ends the program