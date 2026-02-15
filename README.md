# TCG Tracker

# Requirements:
1. Python 3.12 or newer

## How to download TCG Tracker:
1. Navigate to: https://github.com/WillsonX3/SE-2300-Software-Construction
2. Click on TCGTracker.py
3. Locate "Download raw file" button on the upper-right side of the header
4. Press the button to download the program

## How to run TCG Tracker:
1. Locate TCGTracker.py in the Downloads folder
2. Move the program file into a designated folder
3. Right-click on TCGTracker and click "Open"

## How to use TCG Tracker:
- When the program starts, press the ENTER key 
- There will be a menu with five available options:
	1. Add Trading Card
		- Enter card name. Press ENTER when complete.
		- Enter card set. Press ENTER when complete.
		- Enter card value(integer or floating-point numbers only). Press ENTER when complete. 

	2. Edit Trading Card
		- A list of current cards will be listed, along with an index.
		- Select a card by its listed index.
		- There will be a menu with three avaiable options:
			1. Edit card name.
			2. Edit card set.
			3. Edit card value(integer or floating-point numbers only).
		
	3. Delete Trading Card
		- A list of current cards will be listed, along with an index.
		- Select a card by its listed index.
		- Selected card will be deleted.

	4. View Trading Cards
		- All stored cards will be displayed along with their details.
		- Total value of all stored cards will be displayed at the bottom. 

	5. Exit
		- Close the program.

## Additional Information:
- Trading cards and their values will be stored in a JSON file named "cards.json".
	- This file will automatically be created when a card is added
	- This file will be located in the same directory as the program
