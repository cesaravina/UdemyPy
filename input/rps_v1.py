# Basic Rock Paper Scissors game

print("Rock...")
print("Paper...")
print("Scissors...")
#Two Player Game - asks for move as input
player1 = input("Player 1, make your move: ")
player2 = input("Player 2, make your move: ")
# Logic
if player1 == "rock" and player2 == "scissors":
	print("player1 wins!")
elif player1 == "rock" and player2 == "paper":
	print("player2 wins!")
elif player1 == "paper" and player2 == "rock":
	print("player1 wins!")
elif player1 == "paper" and player2 == "scissors":
	print("player2 wins!")
elif player1 == "scissors" and player2 == "rock":
	print("player2 wins!")
elif player1 == "scissors" and player2 == "paper":
	print("player1 wins!")
elif player1 == player2:
	print("it's a tie!")
else:#in case input is anything other than "rock", "paper", or "scissors"
	print("oops, something went wrong!")