# Text-Based Adventure Game

def show_instructions():
    print("""
    Text-Based Adventure Game
    ==========================
    Commands:
      go [direction] (e.g., go north)
      get [item] (e.g., get key)
      inventory (shows collected items)
      quit (exit the game)
    """)

# Room setup
rooms = {
    'Hall': {
        'south': 'Kitchen',
        'east': 'Living Room',
        'item': None
    },
    'Kitchen': {
        'north': 'Hall',
        'item': 'key'
    },
    'Living Room': {
        'west': 'Hall',
        'south': 'Bedroom',
        'item': None
    },
    'Bedroom': {
        'north': 'Living Room',
        'item': 'monster'
    }
}

# Starting position
current_room = 'Hall'
inventory = []

def show_status():
    print("\n---------------------------")
    print(f"You are in the {current_room}.")
    if 'item' in rooms[current_room] and rooms[current_room]['item']:
        if rooms[current_room]['item'] == 'monster':
            print("There is a MONSTER here!")
        else:
            print(f"You see a {rooms[current_room]['item']} here.")
    print("---------------------------")

# Main game loop
def adventure_game():
    show_instructions()
    global current_room
    while True:
        show_status()

        # Get user input
        action = input("What do you want to do? ").lower().split()

        if len(action) < 2:
            if action[0] == "inventory":
                print(f"Your inventory: {inventory}")
            elif action[0] == "quit":
                print("Thanks for playing!")
                break
            else:
                print("Invalid input, try again.")
            continue
        
        command, target = action[0], action[1]

        if command == 'go':
            # Move between rooms
            if target in rooms[current_room]:
                current_room = rooms[current_room][target]
            else:
                print("You can't go that way!")
        
        elif command == 'get':
            # Pick up items
            if 'item' in rooms[current_room] and rooms[current_room]['item'] == target:
                if target == 'monster':
                    print("The monster has caught you! Game Over.")
                    break
                inventory.append(target)
                print(f"You picked up the {target}.")
                rooms[current_room]['item'] = None  # Remove the item from the room
            else:
                print(f"There's no {target} here.")

        else:
            print("Invalid command! Try again.")

        # Check win condition
        if current_room == 'Bedroom' and 'key' in inventory:
            print("You used the key to escape the dungeon. You win!")
            break

if __name__ == "__main__":
    adventure_game()
