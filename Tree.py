import Board
import copy
from math import exp
import random

class Tree:
  #Node (board)
  #Listofchild (list of board)
  def __init__(self, board):
    self.node = board

  def generateChild(self, id):
    listChild = []

    # somebody wins = terminal node
    if (self.node.winCheck() != 0):
      return listChild

    # kalau id bot ini 2, list pion miliknya adalah listPionComp
    if (id == 2):
      listPion = self.node.listPionComp
      # ketika bukan gilirannya, dia akan menjalankan pion lawan
      if (self.node.playerTurn != id): 
        listPion = self.node.listPionUser
    else:
      listPion =self.node.listPionUser
      if (self.node.playerTurn != id):
        listPion = self.node.listPionComp

    # generate semua kemungkinan langkah untuk pion di list
    for p in listPion:
      listMove = self.node.generateMove(p)
      listJump = self.node.generateAllJump(p)

      # append semua kemungkinan jump
      for (x,y) in listJump:
        if self.node.isMoveValid(p,x,y,False):
          child = copy.deepcopy(self.node)
          newP=child.getMatrix()[p.getX()][p.getY()]
          child.move(newP, x, y)
          listChild.append(child)

      # append semua kemungkinan move
      for (x,y) in listMove:
        if self.node.isMoveValid(p,x,y,False):
          child = copy.deepcopy(self.node)
          newP = child.getMatrix()[p.getX()][p.getY()]
          child.move(newP, x, y)
          listChild.append(child) 

    if (self.node in listChild): 
      listChild.remove(self.node)
      
    return listChild

  def generateChildLocal(self, listSize, T, id):
    listChild = []
    if (self.node.winCheck()!=0):
      return listChild
    
    for i in range (listSize):
      child=self.simulatedAnnealing(T, id)
      while (child in listChild):
        child=self.simulatedAnnealing(T, id)
      listChild.append(child)
      
    if (self.node in listChild):
      listChild.remove(self.node)
    return listChild
      
  def simulatedAnnealing(self, T, id):
    listNext = []
    listPion = []
    
    if (id == 2):
      listPion = self.node.listPionComp
      if (self.node.playerTurn!=id): 
        listPion = self.node.listPionUser
    else:
      listPion =self.node.listPionUser
      if (self.node.playerTurn!=id):
        listPion = self.node.listPionComp
    
    # handle kl pion yg kepilih gabisa gerak
    while len(listNext)==0:
      pion = random.choice(listPion)
      listNext = self.node.generateMove(pion)
      for move in listNext:
        x,y = move
        if not self.node.isMoveValid(pion,x,y,False):
          listNext.remove(move)

      listJump = self.node.generateAllJump(pion)
      for move in listJump:
        x,y = move
        if not self.node.isMoveValid(pion,x,y,True):
          listJump.remove(move)

      listNext.extend(listJump)
    
    currentMove = random.choice(listNext)
    listNext.remove(currentMove)
    
    currentBoard = copy.deepcopy(self.node)
    newP= currentBoard.getMatrix()[pion.getX()][pion.getY()]
    x,y = currentMove

    currentBoard.move(newP, x, y)

    # T berkurang secara decrement
    while True:
      if (T==0 or len(listNext)==0):
        return currentBoard
      else:
        nextMove = random.choice(listNext)
        listNext.remove(nextMove)
        nextBoard = copy.deepcopy(self.node)
        newP=nextBoard.getMatrix()[pion.getX()][pion.getY()]
        x,y = nextMove
        nextBoard.move(newP,x,y)
        dE = nextBoard.value(id) - currentBoard.value(id)
        if dE>0:
          currentBoard = nextBoard
        else:
          if (exp(dE/T)>0.5):
            currentBoard = nextBoard
      T-=1

 

