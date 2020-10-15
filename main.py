# Create a Tic Tac Toe game.

# Here are the requirements:

#     2 players should be able to play the game (both sitting at the same computer)
#     The board should be printed out every time a player makes a move
#     You should be able to accept input of the player position and then place a symbol on the board

# Feel free to use Google to help you figure anything out (but don't just Google "Tic Tac Toe in Python" otherwise you won't learn anything!) Keep in mind that this project can take anywhere between several hours to several days.
# If you need help getting started, or are stuck, use steps.txt for a general outline of what this project requires

print("Welcome to the Tic Tac Toe game!")
playerOne = input("Player 1, enter your name: ")
playerTwo = input("Player 2, enter your name: ")
print("---------------------------------------------------")
characterTwo = input(playerTwo + ", would you like to be an X or O(Enter an x or o): ")
if characterTwo.upper() == 'X':
  characterOne = 'O'
  print(playerOne + " your character is "+ characterOne + ". " + playerTwo + " your character is "  + characterTwo + ".")
elif characterTwo.upper() == 'O':
  characterOne = 'X'
  print(playerOne + " your character is "+ characterOne + ". " + playerTwo + " your character is "  + characterTwo + ".")
else:
  print("Invalid answer")

grid = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


print("---------------------------------------------------")
print("Let's get started! "+ playerOne +", you are going first.")
print("Here is the board.")
print(" _________________")
print("|  "+ grid[0] +"  |  "+ grid[1] +"  |  "+ grid[2] +"  |")
print("|_____|_____|_____|")
print("|  "+ grid[3] +"  |  "+ grid[4] +"  |  "+ grid[5] +"  |")
print("|_____|_____|_____|")
print("|  "+ grid[6] +"  |  "+ grid[7] +"  |  "+ grid[8] +"  |")
print("|_____|_____|_____|")

def displayBoard(a, b, c, d, e, f, g, h, i):
  print(" _________________")
  print("|  "+ grid[0] +"  |  "+ grid[1] +"  |  "+ grid[2] +"  |")
  print("|_____|_____|_____|")
  print("|  "+ grid[3] +"  |  "+ grid[4] +"  |  "+ grid[5] +"  |")
  print("|_____|_____|_____|")
  print("|  "+ grid[6] +"  |  "+ grid[7] +"  |  "+ grid[8] +"  |")
  print("|_____|_____|_____|")

position = 0
player = playerOne
character = characterOne
position = int(input(playerOne +  ", which numbered box would you like to place your "+ character + ": "))
grid[position - 1] = character
displayBoard(grid[0], grid[1], grid[2], grid[3], grid[4], grid[5], grid[6], grid[7], grid[8])

def turn(player, character, position):
  print("---------------------------------------------------")
  print(player +", you are next.")
  position = int(input("Which numbered box would you like to place your "+ character + ": "))
  grid[position - 1] = character
  displayBoard(grid[0], grid[1], grid[2], grid[3], grid[4], grid[5], grid[6], grid[7], grid[8])

i = 0
while ( i < 10):
  turn(playerTwo, characterTwo, position)
  i += 1
  if (grid[0] == grid[1] == grid[2]):
    print(playerTwo + " wins!")
    break
  elif (grid[3] == grid[4] == grid[5]):
    print(playerTwo + " wins!")
    break
  elif (grid[6] == grid[7] == grid[8]):
    print(playerTwo + " wins!")
    break
  elif (grid[0] == grid[3] == grid[6]):
    print(playerTwo + " wins!")
    break
  elif (grid[1] == grid[4] == grid[7]):
    print(playerTwo + " wins!")
    break
  elif (grid[2] == grid[5] == grid[8]):
    print(playerTwo + " wins!")
    break
  elif (grid[0] == grid[4] == grid[8]):
    print(playerTwo + " wins!")
    break
  elif (grid[2] == grid[4] == grid[6]):
    print(playerTwo + " wins!")
    break

  turn(playerOne, characterOne, position)
  i += 2
  if (grid[0] == grid[1] == grid[2]):
    print(playerOne + " wins!")
    break
  elif (grid[3] == grid[4] == grid[5]):
    print(playerOne + " wins!")
    break
  elif (grid[6] == grid[7] == grid[8]):
    print(playerOne + " wins!")
    break
  elif (grid[0] == grid[3] == grid[6]):
    print(playerOne + " wins!")
    break
  elif (grid[1] == grid[4] == grid[7]):
    print(playerOne + " wins!")
    break
  elif (grid[2] == grid[5] == grid[8]):
    print(playerOne + " wins!")
    break
  elif (grid[0] == grid[4] == grid[8]):
    print(playerOne + " wins!")
    break
  elif (grid[2] == grid[4] == grid[6]):
    print(playerOne + " wins!")
    break
  
#when position has an X or O make variable == 0, then compare all possible win. eg. 1,2 and 3 are all 0, player wins.
#(1,2,3) (4,5,6) (7,8,9) (1,4,7) (2,5,8) (3,6,9) (1,5,9) (3,5,7)