import numpy as np
import random
from getkey import getkey, keys
import os

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

print("2048 by MChrisGM & GigaHertz")
print("─"*40)

#┌ ┐ ┘ └ ┼ ─ │ ├ ┬ ┤ ┴

#thinspace
# " "

def printGrid():
  print("     A     B     C     D"+"\n  ┌─────┬─────┬─────┬─────┐")
  for i in range(3):
    #print(i+1,"│ "+" │ ".join([b.disp() for b in grid[i]])+" │")
    print(i+1,"│",end="")
    for j in range(4):
      number = grid[i][j].disp()
      n=len(number)
      if n%2:
        print(" "*int((5-n)/2)+number+" "*int((5-n)/2)+"│",end="")
      else:
        print(" "*int(2-n/2)+number[:int(n/2)]+" "+number[int(n/2):]+" "*int(2-n/2)+"│",end="")
    print("\n  ├─────┼─────┼─────┼─────┤")
  print("4 │",end="")  
  for j in range(4):
    number = grid[3][j].disp()
    n=len(number)
    if n%2:
      print(" "*int((5-n)/2)+number+" "*int((5-n)/2)+"│",end="")
    else:
      print(" "*int(2-n/2)+number[:int(n/2)]+" "+number[int(n/2):]+" "*int(2-n/2)+"│",end="")
  print("\n  └─────┴─────┴─────┴─────┘")









def choice():
  i = getkey()
  if i == keys.UP:
    return "u"
  elif i == keys.DOWN:
    return "d"
  elif i == keys.LEFT:
    return "l"
  elif i == keys.RIGHT:
    return "r"
  else:
    return ""
  # return input()

def transposeBlocks(key):
  if key == "u":
    for i in range(4):
      for j in range(1,4):
        zCount = 0
        while grid[j-1-zCount][i].isEmpty():
          zCount += 1
          if j-zCount<1:
            break
        if zCount>0:
          grid[j-zCount][i] = grid[j][i]
          grid[j][i] = block(0)

        if (zCount+j+1) < 4:
          grid[j-zCount-1][i].add(grid[j-zCount][i])
  elif key == "d":
    for i in range(4):
      for j in range(2,-1,-1):
        zCount = 0
        while grid[j+1+zCount][i].isEmpty():
          zCount += 1
          if j+zCount>2:
            break
        if zCount>0:
          grid[j+zCount][i] = grid[j][i]
          grid[j][i] = block(0)

        if (zCount+j+1) < 4:
          grid[j+zCount+1][i].add(grid[j+zCount][i])
  elif key == "l":
    for i in range(4):
      for j in range(1,4):
        zCount = 0
        while grid[i][j-1-zCount].isEmpty():
          zCount += 1
          if j-zCount<1:
            break
        if zCount>0:
          grid[i][j-zCount] = grid[i][j]
          grid[i][j] = block(0)

        if (zCount+j-1) < 4:
          grid[i][j-zCount-1].add(grid[i][j-zCount])
  elif key == "r":
    for i in range(4):
      for j in range(2,-1,-1):
        zCount = 0
        while grid[i][j+1+zCount].isEmpty():
          zCount += 1
          if j+zCount>2:
            break
        if zCount>0:
          grid[i][j+zCount] = grid[i][j]
          grid[i][j] = block(0)

        if (zCount+j+1) < 4:
          grid[i][j+zCount+1].add(grid[i][j+zCount])



def placeRandom():
  global grid
  empty = []
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if grid[i][j].get() == 0:
        empty.append([i,j])
  if len(empty)>0:
    coords = random.choice(empty)
    num = 0
    if random.uniform(0.0,1.0) > 0.9 : num = 4
    else: num = 2
    grid[coords[0]][coords[1]] = block(num)


class block:
  number = 0
  def __init__(self,number):
    self.number = number
  def add(self,block2):
    if self.number == block2.number:
      self.number *= 2
      block2.number = 0
  def disp(self):
    if not self.number:
      return ""
    return str(self.number)
  def get(self):
    if not self.number:
      return 0
    return int(self.number)
  def isEmpty(self):
    return True if not self.number else False

grid = np.empty((4,4),dtype = block)

for i in range(len(grid)):
  for j in range(len(grid[i])):
    grid[i][j] = block(0)

state = "playing"

placeRandom()

while(state != "ended"):  
  cls()
  score = 0
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      score += grid[i][j].get()

  print("Score: "+str(score))
  printGrid()

  before = np.copy(grid)

  while np.array_equal(before, grid):
    key = ""
    while key not in ["u","d","l","r"]:
      key = choice()  
    transposeBlocks(key)
    
  placeRandom()
