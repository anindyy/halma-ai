class Position():
  def __init__(self, pos):
    # TODO: MAKE TWO CONSTRUCTORS
    # Position(pos)
    # Position(x, y)
    self.pos = pos.upper()

  def getY(self):
    if (self.pos[0] == 'A'):
      return 0
    elif (self.pos[0] == 'B'):
      return 1
    elif (self.pos[0] == 'C'):
      return 2
    elif (self.pos[0] == 'D'):
      return 3
    elif (self.pos[0] == 'E'):
      return 4
    elif (self.pos[0] == 'F'):
      return 5
    elif (self.pos[0] == 'G'):
      return 6
    elif (self.pos[0] == 'H'):
      return 7
    elif (self.pos[0] == 'I'):
      return 8
    elif (self.pos[0] == 'J'):
      return 9
    elif (self.pos[0] == 'K'):
      return 10
    elif (self.pos[0] == 'L'):
      return 11
    elif (self.pos[0] == 'M'):
      return 12
    elif (self.pos[0] == 'N'):
      return 13
    elif (self.pos[0] == 'O'):
      return 14
    elif (self.pos[0] == 'P'):
      return 15
      
  def getX(self):
    try:
      return (int(self.pos[1:]) - 1)
    except:
      return ("invalid")

  def convert(self):
    return (self.getX(), self.getY())