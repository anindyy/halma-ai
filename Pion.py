from Position import Position

class Pion:
  def __init__(self, _pos="A0", _player = 0, _inGoal = False, _outHome = False):
    self.pos = Position(_pos)
    self.x = self.pos.getX()
    self.y = self.pos.getY()
    self.occupyplayer = _player # integer
    self.inGoal = _inGoal # boolean
    self.outHome = _outHome # boolean
  
  def reset(self):
    # membuat pion jadi bukan milik salah satu player
    self.occupyplayer = 0
    self.inGoal = False
    self.outHome = False

  def getX(self):
    return self.x

  def setX(self, x):
    self.x = x

  def getY(self):
    return self.y

  def setY(self, y):
    self.y = y

  def getPosition(self):
    return (self.x, self.y)
    
  def setPosition(self, x, y):
    self.x = x
    self.y = y

  def getOccupyPlayer(self):
    return self.occupyplayer
  
  def setOccupyPlayer(self, player):
    self.occupyplayer = player

  def getInGoal(self):
    return self.inGoal

  def getOutHome(self):
    return self.outHome

  # def moveTo(self,x,y):
  #   self.x = x
  #   self.y = y

  def setInGoal(self):
    self.inGoal = True

  def setOutHome(self):
    self.outHome = True
