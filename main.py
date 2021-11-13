from gameComponents import winlose, gameVars, gameResults
from random import randint


# define a win / lose function and invoke it
# in our game loop when lives run out (player or computer)

# save the player as a variable called player
# the value of player will be one of three choices to type (input)
# Boolean values are True or False - you can use these to check state
# and then make programming choices based on their value.


while gameVars.player is False:

    gameVars.player = input("Welcome! Pick between rock, paper, or scissors: ")
    gameResults.computer = gameVars.choices[randint(0, 2)]

    print("~~~~~ You chose: " + gameVars.player + " ~~~~~")
    gameResults.gameResult(gameResults.computer)

    # an array is just a container. It holds multiple values in a 0-based index
    # you can store anything in an array
    # and retrieve it later. Arrays have square bracket notation

    print("Enemy lives: " + str(gameVars.computerLives))
    print("Your lives: " + str(gameVars.playerLives))

    if gameVars.playerLives == 0:
        # call the winorlose function here
        winlose.winorlose("~~~~~ Aw Shucks! You lost!")

    elif gameVars.computerLives == 0:
        # call the winorlose function here
        winlose.winorlose("~~~~~ Congrats! You've won!")

    gameVars.player = False
