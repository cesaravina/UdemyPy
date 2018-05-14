# Basic Rock Paper Scissors game with improved logic. 
print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player 1, make your move: ")
print("*** NO CHEATING PLS ***\n\n" * 21)
player2 = input("Player 2, make your move: ")

# The most likely outcome should be first.
if player1 == player2:
	print("it's a tie!")
elif player1 == "rock":
	if player2 == "scissors":
		print("player2 wins!")
	elif player2 == "paper":
		print("player2 wins!")
elif player1 == "paper":
	if player2 == "rock":
		print("player1 wins!")
	elif player2 == "scissors":
		print("player2 wins!")
elif player1 == "scissors":
	if player2 == "rock":
		print("player2 wins!")
	elif player2 == "paper":
		print("player1 wins!")

else:
	print("oops, something went wrong!")