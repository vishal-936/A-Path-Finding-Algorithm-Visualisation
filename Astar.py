from pygame import * 
import math
from queue import PriorityQueue

Win=display.set_mode((800,800))
display.set_caption("A* Path Finding Algorithm")

RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
WHITE=(255,255,255) #empty space
BLACK=(0,0,0)       #opstacle
PURPLE=(120,0,120)  #color of path 
ORANGE=(255,165,0)  #starting point
GREY=(120,120,120)
TURQUOISE=(64,224,208) #End point

class Spot:
    def __init__(self,row,col,width,total_rows):
        self.row=row
        self.col=col
        self.neighbour=[]
        self.color=WHITE
        self.total_rows=total_rows
        self.x=row*width
        self.y=col*width
        self.width=width

    def get_pos(self):
		return self.row, self.col
    def is_closed(self):
		return self.color == RED
    def is_open(self):
		return self.color == GREEN
    def is_barrier(self):
		return self.color == BLACK
    def is_start(self):
		return self.color == ORANGE
    def is_end(self):
		return self.color == TURQUOISE
    def reset(self):
		self.color = WHITE
    def make_start(self):
		self.color = ORANGE
    def make_closed(self):
		self.color = RED
    def make_open(self):
		self.color = GREEN
    def make_barrier(self):
		self.color = BLACK
    def make_end(self):
		self.color = TURQUOISE
    def make_path(self):
		self.color = PURPLE
    def draw(self, Win):
		draw.rect(Win,self.col,(self.x,self.y,self.width,self.width))
        
       
   

