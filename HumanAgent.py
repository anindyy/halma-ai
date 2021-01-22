from Position import Position
from threading import Timer
from Agent import Agent


class HumanAgent(Agent):
  def __init__(self, id, timelimit):
    super().__init__(id, timelimit)
    

  def play(self, board):
    def validateInput(n):
      nX, nY = n.convert()
      while (nX == "invalid" and n != "end"):
        n = Position(input("Masukkan posisi valid: "))
        nX, nY = n.convert()
      return nX, nY

    n = Position(input("Pion yang ingin dipindahkan: "))
    nX,nY = validateInput(n)

    piece = board.matrix[nX][nY]


    while piece.getOccupyPlayer()!=self.id:
      print("pion tidak valid.")
      n = Position(input("Pion yang ingin dipindahkan: "))
      nX,nY = validateInput(n)
      piece = board.matrix[nX][nY]

    n = Position(input("Pindahkan ke: "))
    nX,nY = validateInput(n)

    validity = board.isMoveValid(piece, nX, nY, False)
    # 0 = invalid; 1 = jump; 2 = move

    while (validity == 0):
      print("Langkah tidak valid. Pilih langkah lain:")
      n = Position(input("Pion yang dipindahkan: "))
      nX,nY = validateInput(n)

      piece = board.matrix[nX][nY]
      n = Position(input("Pindahkan ke: "))
      nX,nY = validateInput(n)

      validity = board.isMoveValid(piece, nX, nY, False)

    if (validity != 0):
      board.move(piece, nX, nY)

    # if move is a jump, player can move again
    if (validity == 1): 
      posX,posY = nX,nY
      while (True):
        board.printBoard()
        piece = board.matrix[posX][posY]
        #print(board.generateAllJump(piece))
        print("Ketik 'end' untuk mengakhiri giliran")
        n = input("Jump lagi ke: ")
                      
        # player decides to end their turn
        if n == "end":
          return
        # player doesnt end their turn
        else: 
          position = Position(n)
          posX, posY = validateInput(position)

        # check validity and move
        if (board.isMoveValid(piece, posX, posY, True)):
          board.move(piece, posX, posY)
        else:
          print("Langkah tidak valid")

    return