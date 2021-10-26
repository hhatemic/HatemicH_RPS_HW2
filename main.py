from random import randint

choices = ["rock", "paper", "scissors"]

# add player and computer lives
playerLives = 5
computerLives = 5

player = False

# define a win / lose function and invoke it
# in our game loop when lives run out (player or computer)


def winorlose(status):
    print("You " + status + "! Would you like to play again?")
    choice = input(" y / n?: ")

    global playerLives
    global computerLives
    global player

    if choice == "n":
        print("better luck next time!")
        exit()
    else:
        #reset and restart the game
        playerLives = 5
        computerLives = 5
        player = False



# save the player as a variable called player
# the value of player will be one of three choices to type (input)
# Boolean values are True or False - you can use these to check state
# and then make programming choices based on their value.


while player is False:


    player = input("Choose rock, paper, or scissors: ")
    computer = choices[randint(0, 2)]

    print("player chose: " + player)

    # an array is just a container. It holds multiple values in a 0-based index
    # you can store anything in an array
    # and retrieve it later. Arrays have square bracket notation



    print("computer chose: " + computer)

    if (computer == player):
        print("tie! try again!")

    elif (player == "rock"):
        if (computer == "paper"):
            print("you lose!")
            playerLives = playerLives - 1
        else:
            print("you win!")
            computerLives = computerLives - 1


    elif (player == "paper"):
        if (computer == "scissors"):
            print("you lose!")
            playerLives = playerLives - 1
        else:
            print("you win!")
            computerLives = computerLives - 1


    elif (player == "scissors"):
        if (computer == "rock"):
            print("you lose!")
            playerLives = playerLives - 1
        else:
            print("you win!")
            computerLives = computerLives - 1

    print("computer lives: " + str(computerLives))
    print("player lives: " + str(playerLives))

    if playerLives == 0:
        # call the winorlose function here
        winorlose("lost")

    elif computerLives == 0:
        # call the winorlose function here
        winorlose("won")

    player = False
