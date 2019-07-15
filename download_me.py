from tkinter import Canvas, Button
from tkinter import Tk
import numpy as np
import sys
import pdb


class TicTacToeEnv():

	metadata = {'render.modes' : ['human']}


	def __init__(self, nb, dw, dh):
		self.nb = nb #nomber of cells in tictactoe fiel
		self.dw = dw #display width
		self.dh = dh #display hight
		self.cell_size = int(self.dw/self.nb) # size of 1 cell  
		self.Move = 1
		self.field = TicTacToeEnv.dataNP(self.nb)
		self.butfield = TicTacToeEnv.dataNN(self.nb)
		self.reword = 0
		self.action_space = TicTacToeEnv.dataNN(self.nb)
		self.count1 = 0
		self.count2 = 0
		self.maxcount = 0 #debug
		self.eteration = 0 #debug 
		self.root = Tk()
		self.can = Canvas(self.root, width=self.dw, height=self.dh)
		self.can.pack() 
		for x in range(0,19):
			for y in range(0,19):
				self.action_space[x][y] = [x, y]

	def step(self, action):
		x, y = action
		self.field[x][y] = self.Move
		done, count1, count2 = TicTacToeEnv.WinCheck(self, self.field, self.butfield, self.Move, x, y)
		TicTacToeEnv.buttonf(self, x, y)
		self.observation_space = self.field
		info = "some info"
		if count1 == 2:
			self.reword += 3
		elif count1 == 3:
			self.reword += 5
		elif count1 ==4:
			self.reword += 7
		elif count1 > 4:
			self.reword = 10
		elif count2 == 3:
			self.reword -= 4
		elif count2 == 4:
			self.reword -= 8
		elif count2 > 4:
			self.reword -= 100
		return self.observation_space, self.reword, done, info






	def reset(self):
		print("reseting...")
		self.field = TicTacToeEnv.dataNP(self.nb)
		for x in range(0,19):
			for y in range(0,19):
				self.butfield[x][y].configure(text = " ", 
											  state = "active", 
											  bg = "white", 
											  fg = "red")
				self.root.update()
		return self.root






	def render(self, mode = 'human', close = False):
		self.root = TicTacToeEnv.CreateField(self) 
		
		







	def CreateField(self):
		TicTacToeEnv.DisplaySetup(self.dw, self.dh, self.root)
		for w in range(0, self.nb):
			self.can.columnconfigure(w, minsize = self.cell_size)
			self.can.rowconfigure(w, minsize = self.cell_size)
			for h in range(0, self.nb):
				self.butfield[w][h] = Button(self.can, bd = 5, 
												  relief = "groove", 
												  text = " ", 
												  fg ='red', 
												  command=lambda w = w, h = h: TicTacToeEnv.buttonf(self.butfield, w, h), 
												  width=2, 
												  height=1)
				self.butfield[w][h].grid(row = w, 
										 column = h)
		return self.root










	def buttonf(self, w, h):
		if self.Move == 1:
			self.butfield[w][h].configure(text = "x", 
										  state = "disabled", 
										  bg = "green", 
										  fg = "red")
			self.field[w, h] = self.Move
			self.Move = -1
		elif self.Move == -1:
			self.butfield[w][h].configure(text = "o", 
										  state = "disabled", 
										  bg = "blue", 
										  fg = "red")
			self.field[w, h] = self.Move
			self.Move = 1
		t = 0
		while t < 10000:
			t += 1









	def WinCheck(self, field, butfield, Move, w, h):
		v = [-1, 1]
		for x in range (-1, 2):
			for y in range (-1, 2):
				count = 1
				stack = []
				stack.append(butfield[w][h])
				for i in v:
					if x == 0 and y == 0:
						continue
					try:
						wa = w
						ha = h
						while field[wa][ha] == field[wa+x*i][ha+y*i] and wa+x*i > 0 and wa+x*i < 18 and ha+y*i > 0 and ha+y*i < 18:
							wa, ha = wa + x*i, ha + y*i
							stack.append(butfield[wa][ha])
							count += 1
							if count >= 5:
								#pdb.set_trace()
								if field[w][h] == 1:
									self.count1 = count
								if field[w][h] == -1:
									self.count2 = count
								while True:
									stack.pop().config(bg = "red", fg = "blue")
									#if len(stack) == 0:
								return True, self.count1, self.count2
						if self.count1 is None:
							self.count1 = 0 
						if self.count2 is None:
							self.count1 = 0
					except:
						continue
		return False, self.count1, self.count2









	def dataNP(nomberOfboxes):
		fieldline = np.array([0]*nomberOfboxes)
		field = np.array([fieldline]*nomberOfboxes)
		return field

	def dataNN(nomberOfboxes):
		field = [[0] * nomberOfboxes for i in range(nomberOfboxes)]
		return field

	def data1D(nomberOfboxes):
		nomberOfboxes = nomberOfboxes*nomberOfboxes
		field = [0]*nomberOfboxes
		return field

	def DisplaySetup(display_width, display_hight, root):
		display_size = "{}x{}".format(display_width, display_hight)
		root.geometry(display_size)
	
