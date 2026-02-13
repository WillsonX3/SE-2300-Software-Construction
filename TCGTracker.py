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
    card_set = input("Enter trading card set: ").strip()
    card_value = input("Enter value of the card: ").strip()

    card_object = Card(card_name, card_set, float(card_value)) #Create a new Card object with the input values

    card_list.append(card_object) #Add the new Card object to the list

    print(f"The following trading card has been added successfully: {card_name}")


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
            print("Editing trading card.")
    
        elif user_input == "3":
            print("Deleting trading card.")
    
        elif user_input == "4":
            print("Viewing trading cards.")
    
        elif user_input == "5":
            break
            
        else:
            print("Please choose a valid option.")

main()
