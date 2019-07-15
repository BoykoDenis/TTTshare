import gym
import tkinter
from gym import error, spaces, utils
from gym.utils import seeding
from tkinter import Canvas, Button
import numpy as np


class TicTacToeEnv(gym.Env):

	metadata = {'render.modes' : ['human']}
	ACTIONS = []
	for x in range(0,19):
		for y in range(0,19):
			ACTIONS.append(str(x)+str(y))
	print(ACTIONS)


	def __init__(self, nb, dw, dh, bfield):
		self.nb = 19 #nomber of cells in tictactoe fiel
		self.dw = dw #display width
		self.dh = dh #display hight
		self.cell_size = int(self.dw/self.nb) # size of 1 cell
		self.root = tkinter.Tk() 
		self.can = tkinter.Canvas(self.root, width=self.dw, height=self.dh)
		self.bfield = bfield
		self.Move = 1
		self.field = dataNP(self.nb)
		self.butfield = dataNN(self.nb)
		self.root = Tk()
		self.can = Canvas(self.root, width=self.dw, height=self.dh)
		self.reword = 0






	def step(self, action):
		w, h = action
		done, count1, count2 = WinCheck(self.field, self.butfield, self.Move, w, h)
		x, y = action
		self.field[x][y] = self.Move
		buttonf(x, y)
		observation_space = self.field
		info = ""
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
		return observation_space, reward, done, info






	def reset(self):
		self.field = dataNP(self.nb)
		for i in self.butfield:
			i.configure(text = " ", 
						state = "enabled", 
						bg = "white", 
						fg = "red")






	def render(self, mode = 'human', close = False):
		CreateField() 
		mainloop()# for tkinter visual rendering all other fonctions should be cald from render method
		# make visualisation of bots moves, by configing buttons 








	def CreateField(self):
		for w in range(0, self.nb):
			can.columnconfigure(w, minsize = self.cell_size)
			can.rowconfigure(w, minsize = self.cell_size)
			for h in range(0, self.nb):
				print("creating a button field...")
				print(self.can)
				self.butfield[w][h] = Button(self.can, bd = 5, 
												  relief = GROOVE, 
												  text = " ", 
												  fg ='red', 
												  command=lambda w = w, h = h: buttonf(self.butfield, w, h), 
												  width=2, 
												  height=1)
				self.butfield[w][h].grid(row = w, 
										 column = h)










	def buttonf(self, w, h):
		if self.Move == 1:
			self.butfield[w][h].configure(text = "x", 
										  state = "disabled", 
										  bg = "green", 
										  fg = "red")
			self.field[w, h] = self.Move
			print(self.field)
			self.Move = -1
		elif self.Move == -1:
			self.butfield[w][h].configure(text = "o", 
										  state = "disabled", 
										  bg = "blue", 
										  fg = "red")
			self.field[w, h] = Move
			print(self.field)
			self.Move = 1
		win = WinCheck(self.field, self.butfield, self.Move*-1, w, h)
		if win != None:
			print("hura player {} won!!!".format(Move))











	def WinCheck(field, butfield, Move, w, h):
		v = [-1, 1]
		count = 0
		for x in range (-1, 2):
			for y in range (-1, 2):
				count = 0
				stack = []
				stack.append(butfield[w][h])
				for i in v:
					if x == 0 and y == 0: # bcs x==0 and y==0 is checking for the same cell so its reason for this if
						continue
					try:
						wa = w
						ha = h
						while field[wa][ha] == field[wa+x*i][ha+y*i] and count < 4:
							wa, ha = wa + x*i, ha + y*i
							stack.append(butfield[wa][ha])
							count += 1
							if count >= 4:
								if field[w][h] == 1:
									count1 = count
								else:
									count2 == count
								print("win")
								while True:
									stack.pop().config(bg = "red", 
													   fg = "blue")
								return True, count1, count2
							else:
								return False, count1, count2
					except:
						continue













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
