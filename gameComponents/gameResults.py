from gameComponents import gameVars


def gameResults(computer):
    print("Computer chose: " + computer)

    if (computer == gameVars.player):
        print("A tie? Try again!")

    elif (gameVars.player == "rock"):
        if (computer == "paper"):
            print("You Lose!")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("You Win!")
            gameVars.computerLives = gameVars.computerLives - 1

    elif (gameVars.player == "paper"):
        if (computer == "scissors"):
            print("You Lose!")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("You Win!")
            gameVars.computerLives = gameVars.computerLives - 1

    elif (gameVars.player == "scissors"):
        if (computer == "rock"):
            print("You Lose!")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("You Win!")
            gameVars.computerLives = gameVars.computerLives - 1
