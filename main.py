from getpass import getpass as input

print("Epic Rock, Paper & Scissors Game")

print()

print("Select your move (R, P or S)")

print()

player1Move = input("Player 1 > ")

print()

player2Move = input("Player 2 > ")

print()

if player1Move == "R":

  if player2Move == "R":
    print("You both picked Rock, draw!")
  elif player2Move == "S":
    print("Player1 smashed Player2's Scissors with Rock!")
  elif player2Move == "P":
    print("Player1's Rock is beaten by Player2's Paper!")
  else:
    print("Invalid Move Player 2!")

elif player1Move == "P":

  if player2Move == "R":
    print("Player2's Rock is beaten by Player1's Paper!")
  elif player2Move == "S":
    print("Player1's Paper is cut by Player2's Scissors!")
  elif player2Move == "P":
    print("Disappointing. Draw.")
  else:
    print("Invalid Move Player 2!")

elif player1Move == "S":

  if player2Move == "R":
    print("Player 2's Rock beats Player1's Scissors")
  elif player2Move == "S":
    print("Scissors bounce off each other. Draw.")
  elif player2Move == "P":
    print("Player1's Scissors destroys Player2's paper!")
  else:
    print("Invalid Move Player 2!")

else:  
  print("Invalid Move Player 1!")

