# Tic-Tac-Toe
OIT coding challenge
import random
top_left = "1"
top_middle = "2"
top_right = "3"
middle_left = "4"
middle_middle = "5"
middle_right = "6"
bottom_left = "7"
bottom_middle = "8"
bottom_right = "9"
command = ""
while True:
    print("Welcome to Tic-Tac-Toe!")
    who_goes_first = input("Would you like to go first? (Y/N): ").lower()
    if who_goes_first == "y":
        print("Enter a number.")
        print("""
    1 2 3
    4 5 6
    7 8 9
            """)
        break
    elif who_goes_first == "n":
        print("""
    0 2 3
    4 5 6
    7 8 9
            """)
        print("Enter a number.")
        break
    else:
        print("I don't understand that...")

while True:
    command = input(">")
    if command == "1":
        top_left = "X"
    elif command == "2":
        top_middle = "X"
    elif command == "3":
        top_right = "X"
    elif command == "4":
        middle_left = "X"
    elif command == "5":
        middle_middle = "X"
    elif command == "6":
        middle_right = "X"
    elif command == "7":
        bottom_left = "X"
    elif command == "8":
        bottom_middle = "X"
    elif command == "9":
        bottom_right = "X"
    else:
        print("I don't understand that...")
    print(f"""
    {top_left} {top_middle} {top_right}
    {middle_left} {middle_middle} {middle_right}
    {bottom_left} {bottom_middle} {bottom_right}
""")
    break
computer_moves = [top_left, top_middle, top_right, middle_left, middle_middle, middle_right, bottom_left, bottom_middle,
                  bottom_right]
computer_moves.sort()

while True:
    command = random.choice(computer_moves)
    if command == "1":
        top_left = "O"
    elif command == "2":
        top_middle = "O"
    elif command == "3":
        top_right = "O"
    elif command == "4":
        middle_left = "O"
    elif command == "5":
        middle_middle = "O"
    elif command == "6":
        middle_right = "O"
    elif command == "7":
        bottom_left = "O"
    elif command == "8":
        bottom_middle = "O"
    elif command == "9":
        bottom_right = "O"
    else:
        print("I don't understand that...")
    print(f"""
    {top_left} {top_middle} {top_right}
    {middle_left} {middle_middle} {middle_right}
    {bottom_left} {bottom_middle} {bottom_right}
""")
    break
while True:
    command = input(">")
    if command == "1":
        top_left = "X"
    elif command == "2":
        top_middle = "X"
    elif command == "3":
        top_right = "X"
    elif command == "4":
        middle_left = "X"
    elif command == "5":
        middle_middle = "X"
    elif command == "6":
        middle_right = "X"
    elif command == "7":
        bottom_left = "X"
    elif command == "8":
        bottom_middle = "X"
    elif command == "9":
        bottom_right = "X"
    else:
        print("I don't understand that...")
    print(f"""
    {top_left} {top_middle} {top_right}
    {middle_left} {middle_middle} {middle_right}
    {bottom_left} {bottom_middle} {bottom_right}
""")
    break
computer_moves = [top_left, top_middle, top_right, middle_left, middle_middle, middle_right, bottom_left, bottom_middle,
                  bottom_right]
computer_moves.sort()

while True:
    command = computer_moves[0]
    if command == "1":
        top_left = "O"
    elif command == "2":
        top_middle = "O"
    elif command == "3":
        top_right = "O"
    elif command == "4":
        middle_left = "O"
    elif command == "5":
        middle_middle = "O"
    elif command == "6":
        middle_right = "O"
    elif command == "7":
        bottom_left = "O"
    elif command == "8":
        bottom_middle = "O"
    elif command == "9":
        bottom_right = "O"
    else:
        print("I don't understand that...")
    print(f"""
    {top_left} {top_middle} {top_right}
    {middle_left} {middle_middle} {middle_right}
    {bottom_left} {bottom_middle} {bottom_right}
""")
    break
while True:
    command = input(">")
    if command == "1":
        top_left = "X"
    elif command == "2":
        top_middle = "X"
    elif command == "3":
        top_right = "X"
    elif command == "4":
        middle_left = "X"
    elif command == "5":
        middle_middle = "X"
    elif command == "6":
        middle_right = "X"
    elif command == "7":
        bottom_left = "X"
    elif command == "8":
        bottom_middle = "X"
    elif command == "9":
        bottom_right = "X"
    else:
        print("I don't understand that...")
    print(f"""
    {top_left} {top_middle} {top_right}
    {middle_left} {middle_middle} {middle_right}
    {bottom_left} {bottom_middle} {bottom_right}
""")
    break
computer_moves = [top_left, top_middle, top_right, middle_left, middle_middle, middle_right, bottom_left, bottom_middle,
                  bottom_right]
computer_moves.sort()

while True:
    command = computer_moves[0]
    if command == "1":
        top_left = "O"
    elif command == "2":
        top_middle = "O"
    elif command == "3":
        top_right = "O"
    elif command == "4":
        middle_left = "O"
    elif command == "5":
        middle_middle = "O"
    elif command == "6":
        middle_right = "O"
    elif command == "7":
        bottom_left = "O"
    elif command == "8":
        bottom_middle = "O"
    elif command == "9":
        bottom_right = "O"
    else:
        print("I don't understand that...")
    print(f"""
    {top_left} {top_middle} {top_right}
    {middle_left} {middle_middle} {middle_right}
    {bottom_left} {bottom_middle} {bottom_right}
""")
    break
while True:
    command = input(">")
    if command == "1":
        top_left = "X"
    elif command == "2":
        top_middle = "X"
    elif command == "3":
        top_right = "X"
    elif command == "4":
        middle_left = "X"
    elif command == "5":
        middle_middle = "X"
    elif command == "6":
        middle_right = "X"
    elif command == "7":
        bottom_left = "X"
    elif command == "8":
        bottom_middle = "X"
    elif command == "9":
        bottom_right = "X"
    else:
        print("I don't understand that...")
    print(f"""
    {top_left} {top_middle} {top_right}
    {middle_left} {middle_middle} {middle_right}
    {bottom_left} {bottom_middle} {bottom_right}
""")
    break
computer_moves = [top_left, top_middle, top_right, middle_left, middle_middle, middle_right, bottom_left, bottom_middle,
                  bottom_right]
computer_moves.sort()

while True:
    command = computer_moves[0]
    if command == "1":
        top_left = "O"
    elif command == "2":
        top_middle = "O"
    elif command == "3":
        top_right = "O"
    elif command == "4":
        middle_left = "O"
    elif command == "5":
        middle_middle = "O"
    elif command == "6":
        middle_right = "O"
    elif command == "7":
        bottom_left = "O"
    elif command == "8":
        bottom_middle = "O"
    elif command == "9":
        bottom_right = "O"
    else:
        print("I don't understand that...")
    print(f"""
    {top_left} {top_middle} {top_right}
    {middle_left} {middle_middle} {middle_right}
    {bottom_left} {bottom_middle} {bottom_right}
""")
    break
while True:
    command = input(">")
    if command == "1":
        top_left = "X"
    elif command == "2":
        top_middle = "X"
    elif command == "3":
        top_right = "X"
    elif command == "4":
        middle_left = "X"
    elif command == "5":
        middle_middle = "X"
    elif command == "6":
        middle_right = "X"
    elif command == "7":
        bottom_left = "X"
    elif command == "8":
        bottom_middle = "X"
    elif command == "9":
        bottom_right = "X"
    else:
        print("I don't understand that...")
    print(f"""
    {top_left} {top_middle} {top_right}
    {middle_left} {middle_middle} {middle_right}
    {bottom_left} {bottom_middle} {bottom_right}
""")
    break
print("You Win!")
print("Thanks for playing!")
