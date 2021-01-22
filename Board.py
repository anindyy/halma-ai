from Pion import Pion
# import copy
from math import inf, sqrt

class Board:
  def __init__(self, size, timelimit):
    self.size = size
    self.timelimit = timelimit
    self.playerTurn = 1
    self.matrix = [[Pion() for i in range (self.size)] for j in range (self.size)]
    self.homeUser = []
    self.homeComp = []
    self.listPionUser = []
    self.listPionComp = []
    # mengisi matriks, listPion, dan home
    for i in range (size):
      for j in range (size):
        self.matrix[i][j].setPosition(i, j)
        if (i + j < (size/2)):
          self.matrix[i][j].setOccupyPlayer(1)
          self.homeUser.append((i,j))
          self.listPionUser.append(self.matrix[i][j])
        elif (i + j >= (3 * size / 2 - 1)):
          self.matrix[i][j].setOccupyPlayer(2)
          self.homeComp.append((i,j))
          self.listPionComp.append(self.matrix[i][j])
    self.listPionComp.reverse()

  def update(self, newboard):
    # digunakan untuk menjalankan pion bot 
    self.matrix = newboard.matrix
    self.listPionUser = newboard.listPionUser
    self.listPionComp = newboard.listPionComp

  def changePlayerTurn(self):
    # mengganti player turn
    if (self.playerTurn == 1):
      self.playerTurn = 2
    else:
      self.playerTurn = 1

  def isOutOfRange(self, x, y): 
    # mengecek apakah posisi x,y melewati index papan permainan
    return (x < 0 or x >= self.size or y < 0 or y >= self.size)
  
  def isFilled(self, x, y):
    # mengecek apakah kotak pada posisi x,y terisi pion
    return (not(self.matrix[x][y].getOccupyPlayer() == 0))

  def posCheck(self, l, x, y):
		# mengecek apakah x, y berada di list
    # l: list homeUser / homeComp
    return (l.count((x,y)) > 0)

  def generateJump(self, p):
    # membuat list berisi tuple (i,j) yang merupakan posisi mana saja kemungkinan pion p melakukan jump
    # return list of tuple
    # melihat pemilik, tujuan, dan letak pion
    player = p.getOccupyPlayer()
    home = []
    goal = []
    if player == 1:
      home = self.homeUser
      goal = self.homeComp
    else:
      home = self.homeComp
      goal = self.homeUser
    checkCoor = (p.getX(),p.getY())

    # proses generate
    listjump = []

    # cek petak di sekitar pion
    for i in range (checkCoor[0]-1,checkCoor[0]+2):
      for j in range (checkCoor[1]-1,checkCoor[1]+2):
        if (not self.isOutOfRange(i,j)):
          if (not (i == checkCoor[0] and j == checkCoor[1])) and self.isFilled(i,j):
            newX = 2 * i - checkCoor[0] 
            newY = 2 * j - checkCoor[1]

            if (not self.isOutOfRange(newX,newY)):
              # mengecek dia keluar dari goal atau balik ke home
              backHome = (home.count(checkCoor) == 0) and (home.count((newX,newY)) > 0)
              outGoal = (goal.count(checkCoor) > 0) and (goal.count((newX,newY)) == 0)
              
              # kalau valid, masuk list jump
              if (not (self.isFilled(newX,newY) or backHome or outGoal)):
                listjump.append((newX,newY))

    return listjump

  def recJump(self, l, x, y):
    newL = self.generateJump(self.matrix[x][y])

    # delete tuple yang ada di newL jika sama dgn tuple di l
    for i in l:
      if newL.count(i) > 0:
        newL.remove(i)
        
    # masukin newL yg ga mungkin sama tuplenya sama l ke l
    l.extend(newL)

    # basis
    if not newL:
      pass
    # rekurens
    else:
      # iterasi untuk generate child dari semua elemen newL
      for j in newL:
        self.recJump(l,j[0],j[1])

  def generateAllJump(self, p):
    # l = self.generateJump(p)
    x,y = p.getPosition()
    l = [(x,y)]
    self.recJump(l, x, y)
    if l.count((x,y)) > 0:
      l.remove((x,y))
    return l

  def generateMove(self, p):
    # membuat list berisi tuple (i,j) yang merupakan posisi mana saja kemungkinan pion p melakukan move
    # return list of tuple
    player = p.getOccupyPlayer()
    home = []
    goal = []
    if player == 1:
      home = self.homeUser
      goal = self.homeComp
    else:
      home = self.homeComp
      goal = self.homeUser
    l = []
    x = p.getX()
    y = p.getY()
    for i in range (x-1,x+2):
      for j in range (y-1,y+2):
        if (not (self.isOutOfRange(i,j))):
          backHome = (home.count((x,y)) == 0) and (home.count((i,j)) > 0)
          outGoal = (goal.count((x,y)) > 0) and (goal.count((i,j)) == 0)
          if (not (self.isFilled(i,j) or backHome or outGoal)):
            l.append((i,j))
    return l

  def move(self, p, x, y):
    # mengganti posisi dari Pion p ke baris x kolom y
    # p Pion, x int, y int
    player = p.getOccupyPlayer()
    a, b = p.getPosition()
    goal = []
    home = []

    # mengubah player pada Pion di matrix[x][y] menjadi milik player yang sedang bermain dan mereset Pion p
    self.matrix[a][b].reset()
    self.matrix[x][y].setOccupyPlayer(player)

    # set inGoal dan outHome Pion p
    # if (not self.posCheck(self.homeComp,x,y) and not self.posCheck(self.homeUser,x,y)):
    #   self.matrix[x][y].setOutHome()
    
    # setting list goal dan home dan menghapus pion pada list pion user atau computer
    if (player == 1):
      home = self.homeUser.copy()
      goal = self.homeComp.copy()
      for i in self.listPionUser:
        if i.getPosition() == (a,b):
          self.listPionUser.remove(i)
          break
      self.listPionUser.append(self.matrix[x][y])
    elif (player == 2):
      home = self.homeComp.copy()
      goal = self.homeUser.copy()
      for i in self.listPionComp:
        if i.getPosition() == (a,b):
          self.listPionComp.remove(i)
          break
      self.listPionComp.append(self.matrix[x][y])
      
    # setting inGoal dan outHome pion tujuan
    if self.posCheck(goal,x,y):
      self.matrix[x][y].setInGoal()
    elif not self.posCheck(home,x,y):
      self.matrix[x][y].setOutHome()

  def isMoveValid(self, p, x, y, jump):
    # p Pion, x int, y int
    # mengecek apakah mengganti posisi Pion p ke baris x kolom y valid sesuai dengan aturan permainan.
		# return 0 jika langkah tidak valid, return 1 jika langkah adalah jump, return 2 jika langkah adalah move
    player = p.getOccupyPlayer()
    a, b = p.getPosition()

    # pion p bukan milik player yang sedang bermain atau input di luar index
    if (player != self.playerTurn or self.isOutOfRange(x,y)):
      print(self.isOutOfRange(x,y))
      print(player,self.playerTurn)
      print(jump)
      return 0

    # else:
    listJump = self.generateAllJump(p)
    listMove = self.generateMove(p)
    inListJump = self.posCheck(listJump,x,y)
    inListMove = self.posCheck(listMove,x,y)

    # bukan jump atau move
    notJumpOrMove = (not inListJump and jump) or not (jump or inListJump or inListMove)

    if (player == 1):
      backHome = p.getOutHome() and self.posCheck(self.homeUser,x,y)
      outGoal = p.getInGoal() and not self.posCheck(self.homeComp,x,y)
    elif (player == 2): 
      backHome = p.getOutHome() and self.posCheck(self.homeComp,x,y)
      outGoal = p.getInGoal() and not self.posCheck(self.homeUser,x,y)

    # posisi tujuan sudah terisi atau kembali ke home base atau keluar dari goal base
    if (self.isFilled(x,y) or backHome or outGoal or notJumpOrMove):
      return 0
    elif (inListJump):
      return 1
    elif (not jump and inListMove):
      return 2

  def winCheck(self):
    # mengecek apakah sudah ada yang memenangkan permainan
		# bernilai 0 jika belum ada pemenang, bernilai 1 jika pengguna yang memenangkan permainan, bernilai 2 jika komputer yang memenangkan permainan
    userWin = True
    compWin = True
    for (x,y) in self.homeUser:
      if (self.matrix[x][y].getOccupyPlayer() != 2): 
        compWin = False
        break
    if compWin:
      return 2
    else:
      for (x,y) in self.homeComp:
        if (self.matrix[x][y].getOccupyPlayer() != 1):
          userWin = False
          break
    if userWin:
      return 1
      
    else:
      return 0  

  def printBoard(self):
    # mencetak board
    a = 'A'
    for i in range (self.size + 1):
      for j in range (self.size + 1):
        if (i == 0):
          if (i == j):
            print('   ', end='')
          else:
            print(str(a),'', end='')
            a = chr(ord(a) + 1)
        elif (j == 0):
          print(str(i).zfill(2), '', end='')
        else:
          print(self.matrix[i-1][j-1].getOccupyPlayer(), '', end='')
      print()
      
  def value(self, id):
    idOpponent = 0
    if id == 1:
      idOpponent = 2
    else:
      idOpponent = 1

    if (self.winCheck() == idOpponent):
      return -inf
    elif (self.winCheck() == id):
      return inf

    valSelf = self.countValue(id)
    valOpponent = self.countValue(idOpponent)

    hasil = - valSelf + valOpponent
    return hasil 


  def countValue(self, player):
    listPion = []
    
    if (player == 2): 
      listPion = self.listPionComp
      x,y = 0,0
    else:
      listPion = self.listPionUser
      n = self.size-1
      x,y = n,n
      
    totalVal = 0

    for pion in listPion:
      add = self.euclideanDist(pion, x, y)
      totalVal += add

    return totalVal

  def euclideanDist(self, pion, x, y):
    distance = sqrt((x - pion.getX())**2 + (y - pion.getY())**2)
    return distance

  def printListPion(self, player):
    if player == 1:
      list = self.listPionUser
    else:
      list = self.listPionComp
    for pion in list:
      print('Pion',pion.getOccupyPlayer(),' (x,y):',pion.getPosition())