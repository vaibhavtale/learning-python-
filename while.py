i = 1

while i <= 5:
    print("*" * i)
    i += 1

print("Done")

secret_num = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Enter a number : "))
    if guess == secret_num :
        print("You won !")
        break
    guess_count += 1
    if(guess_count == guess_limit) :
        print("Ohh You lost !")


# Exercise nostalgic

command = ""
started = False
while True:
    command = input("Enter a command : ").lower()
    if command == "start":
        if started:
            print("car is already started..")
        else:
            print("car started..")
            started = True

    elif command == "help":
        print("""
        start >> to start the car.
        stop >> to stop the car.
        help >> for any suggestion.
        quit >> to quit the game.
        """)
    elif command == "stop":
        if not started:
            print("car is already stopped..")
        else:
            print('car stopped..')
            started = False

    elif command == "quit":
        break
    else:
        print("I didn't get it..")










