from Board import Board
from ComputerAgent import MinimaxAgent, LocalSearchAgent
from HumanAgent import HumanAgent

if __name__ == "__main__":
  print("Welcome to Halma!")
  print()
  Bsize = int(input("Ukuran papan: "))
  timelimit = int(input("Timelimit: "))
  board = Board(Bsize, timelimit)
  print()
  P1 = HumanAgent(1, timelimit)
  P2 = MinimaxAgent(1, timelimit)


  print("Mode Permainan: ")
  print("1. Player vs Player")
  print("2. Player vs Computer")
  print("3. Computer vs Computer")
  mode = int(input("Pilihan mode: "))
  print()

  if mode == 1:
    P1 = HumanAgent(1, timelimit)
    P2 = HumanAgent(2, timelimit)

  elif mode == 2:
    print("1. Merah (Player 1, Atas)")
    print("2. Hijau (Player 2, Bawah)")
    h_player = int((input("Pilihan player: ")))

    if h_player == 1:
      P1 = HumanAgent(1, timelimit)
      print()
      print("Agen Komputer:")      
      print("1. Minimax Agent")
      print("2. Minimax + Local Search Agent")
      agent = int((input("Pilihan agen komputer: ")))

      if agent == 1:
        P2 = MinimaxAgent(1, timelimit)
      else:
        P2 = LocalSearchAgent(1, timelimit)

    else:
      P2 = HumanAgent(2, timelimit)
      print()
      print("Agen Komputer:")
      print("1. Minimax Agent")
      print("2. Minimax + Local Search Agent")
      agent = int((input("Pilihan agen komputer: ")))

      if agent == 1:
        P1 = MinimaxAgent(1, timelimit)
      else:
        P1 = LocalSearchAgent(1, timelimit)

  else:
    print("Jenis Pertandingan:")
    print("1. Minimax vs Minimax")
    print("2. Minimax vs Minimax + Local")
    print("3. Minimax + Local vs Minimax + Local")
    match = int((input("Pilihan pertandingan: ")))

    if match == 1:
      P1 = MinimaxAgent(1, timelimit) 
      P2 = MinimaxAgent(2, timelimit)
    elif match == 2:
      P1 = MinimaxAgent(1, timelimit) 
      P2 = LocalSearchAgent(2, timelimit)
    else:
      P1 = LocalSearchAgent(1, timelimit)
      P2 = LocalSearchAgent(2, timelimit)

  print("~",P1.__class__.__name__, "vs", P2.__class__.__name__, "~")
  print()

  # Game Started
  i=1
  while (True):
        print("ROUND", i)
        print("=== Player 1's turn ===")
        board.printBoard()

        if (P1.__class__.__name__=='LocalSearchAgent'):
          P1.play(board, 30, 30)
        else:
          P1.play(board)
        
        if (board.winCheck() != 0):
          print("player",board.winCheck(),"wins!")
          board.printBoard()
          break

        board.changePlayerTurn()
        
        print("=== Player 2's turn ===")
        board.printBoard()

        if (P2.__class__.__name__=='LocalSearchAgent'):
          P2.play(board, 30, 30)
        else:
          P2.play(board)

        if (board.winCheck() != 0):
          print("player",board.winCheck(),"wins!")
          board.printBoard()
          break

        board.changePlayerTurn()
        i+=1