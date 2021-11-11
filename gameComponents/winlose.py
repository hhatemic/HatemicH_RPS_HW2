from gameComponents import gameVars


def winorlose(status):
    print("Looks like you " + status + "! Would you like to play again?")
    choice = input("[yes] [no]")

    if choice == "no":
        print("better luck next time!")
        exit()
    else:
        # reset and restart the game
        gameVars.playerLives = 5
        gameVars.computerLives = 5
        gameVars.player = False
