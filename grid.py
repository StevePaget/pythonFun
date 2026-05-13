import turtle
import random
import math
import time

def scale(y):
  y = 1-(y + 300)/600
  return y
  
screen = turtle.Screen()
screen.setup(750, 600)
screen.bgcolor("black")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.color("white")
CENTER = 0
YHORIZON = -300


#Rotation Logic
def rotate(x, y, z, angle):
    nx = x
    nz = z
    # Rotate X
    ny = y * math.cos(angle*0.6) - nz * math.sin(angle*0.6)
    nz_old = nz  # ← save it first
    nz = y * math.sin(angle*0.6) + nz_old * math.cos(angle*0.6)
    return nx, ny, nz

def project(point):
    nx, ny, nz = rotate(point[0], point[1], point[2], angle)
    dist = 3# Distance from camera
    factor = 100 / (nz + dist)
    return (nx * factor, ny * factor-300)

class Box:
  def __init__(self,basePoints):
    self.basePoints = basePoints
    self.edges = [[0,1],[1,2],[2,3],[3,0]]


  def update(self,origin):
    self.dist = abs(self.basePoints[0][0]-origin)
    self.height = -0.5*math.sin(self.dist/10)
    if self.height>0:
      self.basePoints[4][2] = self.basePoints[0][2]+self.height
      self.basePoints[5][2] = self.basePoints[1][2]+self.height
      self.basePoints[6][2] = self.basePoints[2][2]+self.height
      self.basePoints[7][2] = self.basePoints[3][2]+self.height
      self.edges = [[0,1],[1,2],[2,3],[3,0],[4,5],[5,6],[6,7],[7,4],[0,4],[1,5],[2,6],[3,7]]
    else:
      self.edges = [[0,1],[1,2],[2,3],[3,0]]
      
      
  def draw(self,angle):
    for edge in self.edges:
        p1, p2 = project(edge[0]), project(edge[1])
        t.penup(); t.goto(p1[0], p1[1]+YHORIZON)
        t.pendown(); t.goto(p2[0], p2[1]+YHORIZON)


def drawGridlines(gridlines):
   for line in gridlines:
      p1, p2 = project(line[0]), project(line[1])
      t.penup(); t.goto(p1)
      t.pendown(); t.goto(p2)

gridlines = []
boxes = []
for i in range(-40,40,2):
  gridlines.append(([-40,i+40,0],[40,i+40,0]))
  gridlines.append(([i,0,0],[i,80,0]))


angle = 0.2
while True:
  t.clear()
  drawGridlines(gridlines)
  screen.update()


  

turtle.done()


