from Agent import Agent
from Tree import Tree
from math import inf
from time import time

class MinimaxAgent(Agent):
  def __init__(self, id, _time):
    super().__init__(id, _time)

  def play(self, board):
    print("MINIMAX PLAYS")
    bestval = board.value(self.id)
    bestboard = board
    deadline = time() + self.time
    #print("current value", bestval)
    cdepth = 0
    while (time() <= deadline):
      print("depth", cdepth)
      finboard, finval = self.minimax(board, True, cdepth, -inf, inf, time() + self.time)
      if (finval > bestval):
        bestval = finval
        bestboard = finboard
      cdepth += 1
    board.update(bestboard)
    #print("new value", self.id, board.value(self.id))

  def minimax(self, board, maximizing, depth, a, b, deadline): 
    moves = Tree(board).generateChild(self.id)   
    bestmove = board

    # a adalah nilai terbaik untuk maximizing (paling besar) sepanjang path ke root
    # b adalah nilai terbaik untuk minimizing (paling kecil) sepanjang path ke root
    if (depth == 0 or len(moves) == 0 or board.winCheck() != 0 or time() > deadline):
      return board, board.value(self.id)
    
    elif (maximizing):        
      bestvalue = -inf
      for m in moves:
        if (time() > deadline):
          return bestmove, bestvalue
        m.changePlayerTurn()
        _, mvalue = self.minimax(m, not maximizing, depth-1, a, b, deadline)
        if (mvalue > bestvalue):
          bestvalue = mvalue
          bestmove = m
        a = max(a, mvalue)
        if (b <= a):
          break
      
    else:
      bestvalue = inf
      for m in moves:
        if (time() > deadline):
          return bestmove, bestvalue
        m.changePlayerTurn()
        _, mvalue = self.minimax(m, not maximizing, depth-1, a, b, deadline)
        if (mvalue < bestvalue):
          bestvalue = mvalue
          bestmove = m
        b = min(b, mvalue)
        if (b <= a):
          break

    return bestmove, bestvalue


class LocalSearchAgent(Agent):
  def __init__(self, id, _time):
    super().__init__(id, _time)

  def play(self,board,listSize,T):
    print("LOCAL SEARCH PLAYS... id =", self.id)
    deadline = time() + self.time
    bestval = board.value(self.id)
    bestboard = board
    cdepth = 0
    while (time() <= deadline):
      print("depth", cdepth)
      finboard, finval = self.minimaxlocal(board, True, cdepth, -inf, inf, time() + self.time, listSize, T)
      if (finval > bestval):
        bestval = finval
        bestboard = finboard
      cdepth+=1
    board.update(bestboard)
    print("value",board.value(self.id))


  def minimaxlocal(self,board,maximizing,depth,a,b,deadline,listSize,T):
    # a adalah nilai terbaik untuk maximizing (paling besar) sepanjang path ke root
    # b adalah nilai terbaik untuk minimizing (paling kecil) sepanjang path ke root
    
    # memanggil simulate untuk generate child 
    moves = Tree(board).generateChildLocal(listSize,T,self.id)
    bestmove = board
    
    if (depth == 0 or len(moves) == 0 or board.winCheck()!=0 or time() > deadline):
      if (time() > deadline):
        print("timeout")
      return board, board.value(self.id)
    
    elif (maximizing):
      bestvalue = -inf
      for m in moves:
        if (time() > deadline):
          #print("timeout at maximizing")
          return bestmove, bestvalue

        m.changePlayerTurn()
        _, mvalue = self.minimaxlocal(m, not maximizing, depth-1, a, b, deadline, listSize, T)
        if (mvalue > bestvalue):
          bestvalue = mvalue
          bestmove = m
        a = max(a, mvalue)

        if (b <= a):
          break

    else:
      bestvalue = inf
      for m in moves:
        if (time() > deadline):
          #print("timeout at minimizing")
          return bestmove, bestvalue

        m.changePlayerTurn()
        _, mvalue = self.minimaxlocal(m, not maximizing, depth-1, a, b, deadline,listSize,T)
        if (mvalue < bestvalue):
          bestvalue = mvalue
          bestmove = m
        b = min(b, mvalue)

        if (b <= a):
          break

    return bestmove, bestmove.value(self.id)

  
    
