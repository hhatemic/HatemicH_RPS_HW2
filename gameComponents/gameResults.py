from gameComponents import gameVars


def gameResult(computer):
    print("~~~~~ Computer chose: " + computer + " ~~~~~")

    if (computer == gameVars.player):
        print("===== A tie? Try again! =====")

    elif (gameVars.player == "rock"):
        if (computer == "paper"):
            print("===== That's not good! =====")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("===== Nice! =====")
            gameVars.computerLives = gameVars.computerLives - 1

    elif (gameVars.player == "paper"):
        if (computer == "scissors"):
            print("===== Uh-Oh! =====")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("===== You're killing it! =====")
            gameVars.computerLives = gameVars.computerLives - 1

    elif (gameVars.player == "scissors"):
        if (computer == "rock"):
            print("===== You're hit! =====")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("===== Good one! =====")
            gameVars.computerLives = gameVars.computerLives - 1
