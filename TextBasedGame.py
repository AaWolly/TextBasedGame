# Text Based Adventure Game

# Welcome statement explaining how the game works and was is expected, along with directions.
def user_instructions():
    print("""Welcome to my game! 
    You must collect all of the items to make the boss happy and win the game. If you fail to collect the 
    items before entering the bosses office, you will be fired. Good luck and have fun!\n""")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")
    print('----------------------------------------------------------------------------------')


# Create the rules of the game and the locations you can go in each room.
rooms = {
    'Lobby': {'North': 'Conference Room', 'West': 'Boss Office', 'East': 'My Office', 'South': 'Server Room'},
    'Boss Office': {'East': 'Lobby', 'Boss': 'Boss'},
    'Conference Room': {'South': 'Lobby', 'East': 'Break Room', 'Item': 'Computer'},
    'Break Room': {'West': 'Conference Room', 'Item': 'Mug'},
    'My Office': {'North': 'Closet', 'West': 'Lobby', 'Item': 'Notes'},
    'Closet': {'South': 'My Office', 'Item': 'Clothes'},
    'Server Room': {'North': 'Lobby', 'East': 'File Room', 'Item': 'Logs'},
    'File Room': {'West': 'Server Room', 'Item': 'Files'}
}

# List to track inventory
inventory = []

# Set current room to 'Lobby' and inventory = 0
currentRoom = 'Lobby'

# Result of last move
msg = ""

user_instructions()

# Create your gameplay loop
while True:
    print(f'You are in the {currentRoom}\nInventory : {inventory}\n{'-' * 27}')
    # Display msg
    print(msg)

    if 'Item' in rooms[currentRoom].keys():
        nearby_item = rooms[currentRoom]['Item']
        if nearby_item not in inventory:
            if nearby_item[-1] == 's':
                print(f'You see the {nearby_item}')
            else:
                print(f'You see a {nearby_item}')
    # Boss encounter
    if 'Boss' in rooms[currentRoom].keys():
        if len(inventory) < 6:
            print(f"You're Fired!!")
            break

        else:
            print(f'You survive another day.')
            break

    # Accepts the players move as an input
    user_input = input('Enter your move:\n')

    # Splits move into input
    next_move = user_input.split(' ')

    # First word is the action, can use all lower case or upper case
    action = next_move[0].title()

    # Reset the item and direction
    item = 'Item'
    direction = 'null'

    if len(next_move) > 1:
        item = next_move[1:]
        direction = next_move[1].title()

        item = ' '.join(item).title()

    # Moving between the rooms
    if action == 'Go':
        try:
            currentRoom = rooms[currentRoom][direction]
            msg = f'You traveled {direction}.'

        except:
            msg = f'Invalid move.'

    # Picking up items
    elif action == 'Get':
        try:
            if item == rooms[currentRoom]["Item"]:

                if item not in inventory:

                    inventory.append(rooms[currentRoom]["Item"])
                    msg = f"{item} retrieved!"

                else:
                    msg = f"You already have the {item}"

            else:
                msg = f"Can't find {item}"

        except:
            msg = f"Can't find {item}"

    # Exiting the game
    elif action == 'Exit':
        break

    # Any other commands
    else:
        msg = 'Invalid Command'
