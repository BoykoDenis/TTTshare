from tictactoe_env import TicTacToeEnv as MEnv #main env
import random
import tkinter as tk
#import sys
#import pdb

env = MEnv(19, 650, 650)
arraybackup = env.action_space
for epoch in range (0, 2):
	env.render()
	#print("reset")
	root = env.reset()
	arrayCount = 0
	for ev in range (0, 361):
		action = random.choice(random.choice(env.action_space))
		if action == None:
			if arrayCount < 361:
				while action is None:
					action = random.choice(random.choice(env.action_space))
			else:
				env.action_space = arraybackup
				continue
		a, b = action
		arrayCount +=1
		env.action_space[a][b] = None
		observation, reword, done, info = env.step(action)
		#print(done)
		if done == True:
			#print("True, reset")
			continue
		root.update()
