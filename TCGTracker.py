print("Welcome to your TCG Tracker!\n")

user_input = input("Press ENTER to continue...")

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
            print("Adding trading card.")

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
