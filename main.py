import random

def check_input(player_input):
  player_input = player_input.upper()
  pos_move = ["ROCK", "PAPER", "SCISSORS"]

  for move in pos_move:
    if move == player_input:
      return True

  return False



def check_yn(answer):
  answer = answer.upper()
  pos_ans = ["YES", "Y"]

  for ans in pos_ans:
    if ans == answer:
      return True

  return False

  

def win_condition(player_input, ai_input):
  win_con = {"ROCK": "SCISSORS", "SCISSORS": "PAPER", "PAPER":"ROCK"}

  if player_input == ai_input:
    return 0
  else:
    for check in win_con:
      if player_input == check and ai_input == win_con[check]:
        return 1
      elif ai_input == check and player_input == win_con[check]:
        return 2



game = 0

ai_pos = ["ROCK", "PAPER", "SCISSORS"]

while game == 0:

  player_move = input("Enter Rock, Paper or Scissors: ")

  player_move = player_move.upper()

  if check_input(player_move) is True:

    ai_move = random.randint(0,2)
    ai_move = ai_pos[ai_move]

    print("You entered " + player_move)
    print("The computer entered " + ai_move)

    winner = win_condition(player_move, ai_move)

    if winner == 0:
      print("The game was a draw please enter again.")
    elif winner == 1:
      print(player_move + " beats " + ai_move + "!")
      print("You have won well done!")

      if check_yn(input("Do you wish to play again: ")) is True:
        print("Restarting game...")
      else:
        print("Ending game...")
        game = 1

    elif winner == 2:
      print(ai_move + " beats " + player_move + "!")
      print("The computer has won sorry.")

      if check_yn(input("Do you wish to play again: ")) is True:
        print("Restarting game...")
      else:
        print("Ending game...")
        game = 1

  else: 
    print("please enter another move")
