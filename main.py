
import random
from bke import EvaluationAgent, start, can_win, is_winner, opponent, train, load, start, save

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

class MyRandomAgent(EvaluationAgent):
  def evaluate(self, board, my_symbol, opponent_symbol):
    return random.randint(1, 500)

class MyAgent(MLAgent):
  def evaluate(self, board):
      if is_winner(board, self.symbol):
          reward = 1
      elif is_winner(board, opponent[self.symbol]):
          reward = -1
      else:
          reward = 0
      return reward

def tegenMens():
    start()

def tegenSlim():
    my_agent = load('MyAgent_3000')
    start(player_o=my_agent)

def tegenDom():
  random_opponent = MyRandomAgent()
  start(player_o=random_opponent)

def TrainTegenstander():
    my_agent = MyAgent(alpha=0.8, epsilon=0.2)
   
    train(my_agent, 3000)
 
    my_agent.learning = True
 
    save(my_agent, 'MyAgent_3000')

def game():
  print("typ 'a' voor 2 spelers")
  print("typ 'b' voor slimme tegenstader")
  print("typ 'c' voor domme tegenstander")
  print("typ 'd' voor een tegenstander trainen")
  i = input("voer hier in:") 
   
mijn_speler = MijnSpeler()
  random_opponent = MyRandomAgent()
 
  if i == "a":
    tegenMens()
 
  if i == "b":
    tegenSlim()
 
  if i == "c":
    tegenDom()

  if i == "d":
    TrainTegenstander()
   
  else:
   print("voer a, b, c of d in alsjeblieft")
   game()
 
game()