from gameComponents import gameVars


def winorlose(status):
    print(status + " Would you like to play again? ~~~~~")
    choice = input("-----[yes]---[no]----- ")

    if choice == "no":
        print("===== That was fun! I hope I see you soon! =====")
        exit()
    else:
        # reset and restart the game
        gameVars.playerLives = 2
        gameVars.computerLives = 2
        gameVars.player = False
