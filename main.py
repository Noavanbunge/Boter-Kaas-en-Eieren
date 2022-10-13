
import random
from bke import EvaluationAgent, start, can_win

def game():
  print("typ 'a' voor 2 spelers")
  print("typ 'b' voor slimme tegenstader")
  print("typ 'c' voor domme tegenstander")
  i = input("voer hier in:")


  class MijnSpeler(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
      getal = 1
      if can_win(board, opponent_symbol):
        getal = getal -1000
      if can_win(board, my_symbol):
        getal = getal +1000
      if board[4] == my_symbol:
        getal = getal +5
      if board[4] == opponent_symbol:
        getal = getal -5
      return getal