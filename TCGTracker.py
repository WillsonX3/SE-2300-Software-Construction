print("Welcome to your TCG Tracker!\n")

user_input = input("Press ENTER to continue...")

card_list = []

class Card:
    def __init__(self, card_name, card_set, card_value): #Constructor method - initializes object's values from the given arguments
        self.card_name = card_name
        self.card_set = card_set
        self.card_value = card_value

def add_card():
    card_name = input("Enter trading card name: ").strip()

    if card_name == "": #If invalid, return to main
        print("Trading card name cannot be empty.")
        return
    
    card_set = input("Enter trading card set: ").strip()

    if card_set == "":
        print("Trading card set cannot be empty.")
        return
    
    try:
        card_value = float(input("Enter value of the card: "))
    
    except ValueError: # If wrong data type is entered

        print("Please enter a number.")
        return



    card_object = Card(card_name, card_set, card_value) #Create a new Card object with the input values

    card_list.append(card_object) #Add the new Card object to the list

    print(f"The following trading card has been added successfully: {card_name}")

    
def retrieve_cards():

    if card_list == []:

        print("Your card list is empty.")
        return

    print(f"**Your current card list**\n")

    number = 1
    total_value = 0

    for card in card_list: #Iterate through each index of card_list

        print(f"{number} - Card: {card.card_name} | Set: {card.card_set} | Value: ${card.card_value}")
        number += 1
        total_value += card.card_value

    print(f"\nTotal value of your cards: ${total_value}")

def delete_card():

    if card_list == []:

        print("Your card list is empty.")
        return
    
    index = 0

    for card in card_list: #Iterate through card_list to display a card in their respective index
        
        print(f"{index} - Card: {card.card_name}")
        index += 1
    
    print("Please choose the index of the card you want to delete.")

    try:

        user_input = int(input())

        if user_input < 0 or user_input >= len(card_list): #If the user input is outside the bounds of index, then...

            print("Please enter a valid index.")
            return

    except ValueError:

        print("Please enter a number.")
        return
    
    

    print(f"You have successfully deleted card: {card_list[user_input].card_name}")

    card_list.pop(user_input) #Removes the index requested from user
    
def edit_card():

    if card_list == []:

        print("Your card list is empty.")
        return
    
    index = 0

    for card in card_list: 
        
        print(f"{index} - Card: {card.card_name}")
        index += 1
    
    print("Please choose the index of the card you want to edit.")

    try:

        user_input = int(input())

        if user_input < 0 or user_input >= len(card_list):

            print("Please enter a valid index.")
            return
    
    except ValueError:

        print("Please enter a number.")
        return
    
    print(f"The following card has been selected: {card_list[user_input].card_name}")
    
    selected_index = user_input #Save user selected index to reference later


    print("\nPlease choose an option below:")
    print("1. Edit Card Name")
    print("2. Edit Card Set")
    print("3. Edit Card Value")

    user_input = input("Choose the option you would like to change: ")

    if user_input == "1":

        print("Enter trading card name: ")

        user_input = input().strip()

        card_list[selected_index].card_name = user_input

        print(f"Card name has been changed successfully to: {user_input}")

    elif user_input == "2":

        print("Enter trading card set: ")

        user_input = input().strip()

        card_list[selected_index].card_set = user_input

        print(f"Card set has been changed successfully to: {user_input}")

    elif user_input == "3":

        print("Enter trading card value: ")

        try:

            user_input = int(input())

            card_list[selected_index].card_value = user_input

            print(f"Card value has been changed successfully to: ${user_input}")
        
        except ValueError:
            print("Please enter a number.")
            return

    else:
        print("That is not a valid option.")

    



def main():

    while True:

        print("\nPlease choose an option below:")
        print("1. Add Trading Card")
        print("2. Edit Trading Card")
        print("3. Delete Trading Card")
        print("4. View Trading Cards")
        print("5. Exit")

        user_input = input("Option: ")

        if user_input == "1":
            #print("Adding trading card.")
            add_card()

        elif user_input == "2":
            #print("Editing trading card.")
            edit_card()
    
        elif user_input == "3":
            #print("Deleting trading card.")
            delete_card()
    
        elif user_input == "4":
            #print("Viewing trading cards.")
            retrieve_cards()
            
    
        elif user_input == "5":
            break
            
        else:
            print("Please choose a valid option.")

main()
