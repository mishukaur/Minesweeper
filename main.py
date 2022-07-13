import random	


row1 = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
row2 = ["1", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
row3 = ["2", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
row4 = ["3", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
row5 = ["4", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
row6 = ["5", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
row7 = ["6", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
row8 = ["7", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
row9 = ["8", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
row10 = ["9", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
row11 = ["10", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]

hrow1 = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
hrow2 = ["1", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
hrow3 = ["2", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
hrow4 = ["3", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
hrow5 = ["4", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
hrow6 = ["5", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
hrow7 = ["6", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
hrow8 = ["7", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
hrow9 = ["8", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
hrow10 = ["9", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
hrow11 = ["10", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]

frow1 = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
frow2 = ["1", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
frow3 = ["2", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
frow4 = ["3", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
frow5 = ["4", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
frow6 = ["5", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
frow7 = ["6", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
frow8 = ["7", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
frow9 = ["8", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
frow10 = ["9", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
frow11 = ["10", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]

def makeboard():
	print(row1)
	print(row2)
	print(row3)
	print(row4)
	print(row5)
	print(row6)
	print(row7)
	print(row8)
	print(row9)
	print(row10)
	print(row11)

def makehboard():
	print(hrow1)
	print(hrow2)
	print(hrow3)
	print(hrow4)
	print(hrow5)
	print(hrow6)
	print(hrow7)
	print(hrow8)
	print(hrow9)
	print(hrow10)
	print(hrow11)

def makefboard():
	print(frow1)
	print(frow2)
	print(frow3)
	print(frow4)
	print(frow5)
	print(frow6)
	print(frow7)
	print(frow8)
	print(frow9)
	print(frow10)
	print(frow11)


hboard = [(hrow1), (hrow2), (hrow3), (hrow4), (hrow5), (hrow6), (hrow7), (hrow8), (hrow9), (hrow10), (hrow11)]

fboard = [(frow1), (frow2), (frow3), (frow4), (frow5), (frow6), (frow7), (frow8), (frow9), (frow10), (frow11)]

board = [(row1), (row2), (row3), (row4), (row5), (row6), (row7), (row8), (row9), (row10), (row11)]

for i in range(10):
	x = random.randrange(1,11)
	y = random.randrange(1,11)
	if board[x][y] == "*":
		pass
	elif board[x][y] == "_":
		board[x][y] = "*"

def hboard_for_visible():
	for i in range(10):
		x = random.randrange(1,11)
		y = random.randrange(1,11)
		if hboard[x][y] == "*":
			pass
		elif hboard[x][y] == "_":
			hboard[x][y] = "*"
		

for x in range(1,11):
	for y in range(1,11):
		if board[x][y] == "*":
			pass
		elif board[x][y] == "_":
			if x < 10 and y < 10:
				if board[x-1][y] == "*" and board[x][y-1] == "*" and board[x][y+1] == "*":
					board[x][y] = "3"
				if board[x+1][y] == "*" and board[x][y-1] == "*" and board[x][y+1] == "*":
					board[x][y] = "3"
				if board[x-1][y] == "*" and board[x+1][y] == "*" and board[x][y-1] == "*":
					board[x][y] = "3"
				if board[x-1][y] == "*" and board[x+1][y] == "*" and board[x][y+1] == "*":
					board[x][y] = "3"
				if board[x][y+1] == "*" and board[x][y-1] == "*" and board[x][y] != "3":
					board[x][y] = "2" 
				if board[x+1][y] == "*" and board[x-1][y] == "*" and board[x][y] != "3":
					board[x][y] = "2" 
				if board[x-1][y] == "*" and board[x][y-1] == "*" and board[x][y] != "3":
					board[x][y] = "2" 
				if board[x-1][y] == "*" and board[x][y+1] == "*" and board[x][y] != "3":
					board[x][y] = "2" 
				if board[x+1][y] == "*" and board[x][y-1] == "*" and board[x][y] != "3":
					board[x][y] = "2" 
				if board[x+1][y] == "*" and board[x][y+1] == "*" and board[x][y] != "3":
					board[x][y] = "2" 
				if board[x+1][y] == "*" and board[x][y] != "2" and board[x][y] != "3":
					board[x][y] = "1"
				if board[x-1][y] == "*" and board[x][y] != "2" and board[x][y] != "3":
					board[x][y] = "1"
				if board[x][y+1] == "*" and board[x][y] != "2" and board[x][y] != "3":
					board[x][y] = "1"
				if board[x][y-1] == "*" and board[x][y] != "2" and board[x][y] != "3":
					board[x][y] = "1"
			elif x == 10 and y < 10:
				if board[x-1][y] == "*" and board[x][y-1] == "*" and board[x][y+1] == "*":
					board[x][y] = "3"
				if board[x][y+1] == "*" and board[x][y-1] == "*" and board[x][y] != "3":
					board[x][y] = "2" 
				if board[x-1][y] == "*" and board[x][y+1] == "*" and board[x][y] != "3":
					board[x][y] = "2" 
				if board[x-1][y] == "*" and board[x][y-1] == "*" and board[x][y] != "3":
					board[x][y] = "2" 
				if board[x-1][y] == "*" and board[x][y] != "2" and board[x][y] != "3":
					board[x][y] = "1"
				if board[x][y+1] == "*" and board[x][y] != "2" and board[x][y] != "3":
					board[x][y] = "1"
				if board[x][y-1] == "*" and board[x][y] != "2" and board[x][y] != "3":
					board[x][y] = "1"
			elif y == 10 and x < 10:
				if board[x-1][y] == "*" and board[x+1][y] == "*" and board[x][y-1] == "*":
					board[x][y] = "3"
				if board[x+1][y] == "*" and board[x-1][y] == "*" and board[x][y] != "3":
					board[x][y] = "2" 
				if board[x-1][y] == "*" and board[x][y-1] == "*" and board[x][y] != "3":
					board[x][y] = "2" 
				if board[x+1][y] == "*" and board[x][y] != "2" and board[x][y] != "3":
					board[x][y] = "1"
				if board[x-1][y] == "*" and board[x][y] != "2" and board[x][y] != "3":
					board[x][y] = "1"
				if board[x][y-1] == "*" and board[x][y] != "2" and board[x][y] != "3":
					board[x][y] = "1"
			elif x == 10 and y == 10:
				if board[x-1][y] == "*" and board[x][y-1] == "*":
					board[x][y] = "2"
				if board[x-1][y] == "*" and board[x][y] != "2" and board[x][y] != "3":
					board[x][y] = "1"
				if board[x][y-1] == "*" and board[x][y] != "2" and board[x][y] != "3":
					board[x][y] = "1"
          
          
def gameloop():
	gamestate = "game"
	minechecker = 0
	gamemode = input("Would you like to play in hidden or visible mode?: ")
	if gamemode == "visible":
		makeboard()
		hboard_for_visible()
		for s in range(11):
			for t in range(11):
				if hboard[s][t] == "*":
					minechecker += 1
		while gamestate == "game":
			fchecker = 0
			for q in range(11):
				for r in range(11):
					if board[q][r] == "F":
						fchecker += 1

			if "*" not in (board) and fchecker == minechecker:
				print("You win!")
				gamestate = "exit"
				break

			choice = input("Would you like to place or remove a flag, or reveal a location. Type 'f' for the first two options, or 'r' for the second option: ")
			if choice == "f":
				foption = input("Would you like to place or remove a flag? Type 'p' to place a flag or 'r' to remove a flag: ")
				if foption == "p":
					guess = input("Where would you like to place a flag? Type in the column number first and then the row number, space in between: ")
					placement = guess.split()	
					for x in range(11):
						if placement[0] == row1[x] and placement[1] == row2[0]:
							row2[x] = "F"
							makeboard()
						if placement[0] == row1[x] and placement[1] == row3[0]:
							row3[x] = "F"
							makeboard()
						if placement[0] == row1[x] and placement[1] == row4[0]:
							row4[x] = "F"
							makeboard()
						if placement[0] == row1[x] and placement[1] == row5[0]:
							row5[x] = "F"
							makeboard()
						if placement[0] == row1[x] and placement[1] == row6[0]:
							row6[x] = "F"
							makeboard()
						if placement[0] == row1[x] and placement[1] == row7[0]:
							row7[x] = "F"
							makeboard()
						if placement[0] == row1[x] and placement[1] == row8[0]:
							row8[x] = "F"
							makeboard()
						if placement[0] == row1[x] and placement[1] == row9[0]:
							row9[x] = "F"
							makeboard()
						if placement[0] == row1[x] and placement[1] == row10[0]:
							row10[x] = "F"
							makeboard()
						if placement[0] == row1[x] and placement[1] == row11[0]:
							row11[x] = "F"
							makeboard()
				elif foption == "r":
					pass
			elif choice == "r":
				reveal = input("Which spot would you like to reveal? Type in the column number first and then the row number, space in between: ")
				rplace = reveal.split()
				for x in range(11):
						if rplace[0] == row1[x] and rplace[1] == row2[0] and row2[x] != "F":
							if row2[x] == "*":
								makeboard()
								print("You lose!")
								gamestate = "done"
								break
							elif row2[x] == "_":
								row2[x] = "R"
								makeboard()
							elif row2[x] == "1":
								pass
							elif row2[x] == "2":
								pass
							elif row2[x] == "3":
								pass
						if rplace[0] == row1[x] and rplace[1] == row3[0] and row3[x] != "F":
							if row3[x] == "*":
								makeboard()
								print("You lose!")
								gamestate = "done"
								break
							elif row3[x] == "_":
								row3[x] = "R"
								makeboard()
							elif row3[x] == "1":
								pass
							elif row3[x] == "2":
								pass
							elif row3[x] == "3":
								pass
						if rplace[0] == row1[x] and rplace[1] == row4[0] and row4[x] != "F":
							if row4[x] == "*":
								makeboard()
								print("You lose!")
								gamestate = "done"
								break
							elif row4[x] == "_":
								row4[x] = "R"
								makeboard()
							elif row4[x] == "1":
								pass
							elif row4[x] == "2":
								pass
							elif row4[x] == "3":
								pass
						if rplace[0] == row1[x] and rplace[1] == row5[0] and row5[x] != "F":
							if row5[x] == "*":
								makeboard()
								print("You lose!")
								gamestate = "done"
								break
							elif row5[x] == "_":
								row5[x] = "R"
								makeboard()
							elif row5[x] == "1":
								pass
							elif row5[x] == "2":
								pass
							elif row5[x] == "3":
								pass
						if rplace[0] == row1[x] and rplace[1] == row6[0] and row6[x] != "F":
							if row6[x] == "*":
								makeboard()
								print("You lose!")
								gamestate = "done"
								break
							elif row6[x] == "_":
								row6[x] = "R"
								makeboard()
							elif row6[x] == "1":
								pass
							elif row6[x] == "2":
								pass
							elif row6[x] == "3":
								pass
						if rplace[0] == row1[x] and rplace[1] == row7[0] and row7[x] != "F":
							if row7[x] == "*":
								makeboard()
								print("You lose!")
								gamestate = "done"
								break
							elif row7[x] == "_":
								row7[x] = "R"
								makeboard()
							elif row7[x] == "1":
								pass
							elif row7[x] == "2":
								pass
							elif row7[x] == "3":
								pass
						if rplace[0] == row1[x] and rplace[1] == row8[0] and row8[x] != "F":
							if row8[x] == "*":
								makeboard()
								print("You lose!")
								gamestate = "done"
								break
							elif row8[x] == "_":
								row8[x] = "R"
								makeboard()
							elif row8[x] == "1":
								pass
							elif row8[x] == "2":
								pass
							elif row8[x] == "3":
								pass
						if rplace[0] == row1[x] and rplace[1] == row9[0] and row9[x] != "F":
							if row9[x] == "*":
								makeboard()
								print("You lose!")
								gamestate = "done"
								break
							elif row9[x] == "_":
								row9[x] = "R"
								makeboard()
							elif row9[x] == "1":
								pass
							elif row9[x] == "2":
								pass
							elif row9[x] == "3":
								pass
						if rplace[0] == row1[x] and rplace[1] == row10[0] and row10[x] != "F":
							if row10[x] == "*":
								makeboard()
								print("You lose!")
								gamestate = "done"
								break
							elif row10[x] == "_":
								row10[x] = "R"
								makeboard()
							elif row10[x] == "1":
								pass
							elif row10[x] == "2":
								pass
							elif row10[x] == "3":
								pass
						if rplace[0] == row1[x] and rplace[1] == row11[0] and row11[x] != "F":
							if row11[x] == "*":
								makeboard()
								print("You lose!")
								gamestate = "done"
								break
							elif row11[x] == "_":
								row11[x] = "R"
								makeboard()
							elif row11[x] == "1":
								pass
							elif row11[x] == "2":
								pass
							elif row11[x] == "3":
								pass
	elif gamemode == "hidden":
		makehboard()
		for f in range(1, 11):
			for g in range(1, 11):
				if board[f][g] == "1":
					fboard[f][g] = "1"
				if board[f][g] == "2":
					fboard[f][g] = "2"
				if board[f][g] == "3":
					fboard[f][g] = "3"
		while gamestate == "game":
			if fboard == board:
				print("You win!")
				gamestate = "exit"
				break
			fcounter = 0
			choice = input("Would you like to place or remove a flag, or reveal a location. Type 'f' for the first two options, or 'r' for the second option: ")
			if choice == "f":
				foption = input("Would you like to place or remove a flag? Type 'p' to place a flag or 'r' to remove a flag: ")
				if foption == "p":
					guess = input("Where would you like to place a flag? Type in the column number first and then the row number, space in between: ")
					placement = guess.split()	
					if fcounter >= 10:
						print("You have too many flags! Remove one to place another.")
					if fcounter < 10:
						for x in range(11):
							if placement[0] == hrow1[x] and placement[1] == hrow2[0]:
								hrow2[x] = "F"
								frow2[x] = "*"
								fcounter += 1
								makehboard()
							if placement[0] == hrow1[x] and placement[1] == hrow3[0]:
								hrow3[x] = "F"
								frow3[x] = "*"
								fcounter += 1
								makehboard()
							if placement[0] == hrow1[x] and placement[1] == hrow4[0]:
								hrow4[x] = "F"
								frow4[x] = "*"
								fcounter += 1
								makehboard()
							if placement[0] == hrow1[x] and placement[1] == hrow5[0]:
								hrow5[x] = "F"
								frow5[x] = "*"
								fcounter += 1
								makehboard()
							if placement[0] == hrow1[x] and placement[1] == hrow6[0]:
								hrow6[x] = "F"
								frow6[x] = "*"
								fcounter += 1
								makehboard()
							if placement[0] == hrow1[x] and placement[1] == hrow7[0]:
								hrow7[x] = "F"
								frow7[x] = "*"
								fcounter += 1
								makehboard()
							if placement[0] == hrow1[x] and placement[1] == hrow8[0]:
								hrow8[x] = "F"
								frow8[x] = "*"
								fcounter += 1
								makehboard()
							if placement[0] == hrow1[x] and placement[1] == hrow9[0]:
								hrow9[x] = "F"
								frow9[x] = "*"
								fcounter += 1
								makehboard()
							if placement[0] == hrow1[x] and placement[1] == hrow10[0]:
								hrow10[x] = "F"
								frow10[x] = "*"
								fcounter += 1
								makehboard()
							if placement[0] == hrow1[x] and placement[1] == hrow11[0]:
								hrow11[x] = "F"
								frow11[x] = "*"
								fcounter += 1
								makehboard()
					if foption == "r":
						if fcounter < 1:
							print("You don't have any flags!")
						if fcounter >= 1:
							for x in range(11):
									if placement[0] == hrow1[x] and placement[1] == hrow2[0]:
										hrow2[x] = "_"
										frow2[x] = "_"
										fcounter -= 1
										makehboard()
									if placement[0] == hrow1[x] and placement[1] == hrow3[0]:
										hrow3[x] = "_"
										frow3[x] = "_"
										fcounter -= 1
										makehboard()
									if placement[0] == hrow1[x] and placement[1] == hrow4[0]:
										hrow4[x] = "_"
										frow4[x] = "_"
										fcounter -= 1
										makehboard()
									if placement[0] == hrow1[x] and placement[1] == hrow5[0]:
										hrow5[x] = "_"
										frow5[x] = "_"
										fcounter -= 1
										makehboard()
									if placement[0] == hrow1[x] and placement[1] == hrow6[0]:
										hrow6[x] = "_"
										frow6[x] = "_"
										fcounter -= 1
										makehboard()
									if placement[0] == hrow1[x] and placement[1] == hrow7[0]:
										hrow7[x] = "_"
										frow7[x] = "_"
										fcounter -= 1
										makehboard()
									if placement[0] == hrow1[x] and placement[1] == hrow8[0]:
										hrow8[x] = "_"
										frow8[x] = "_"
										fcounter -= 1
										makehboard()
									if placement[0] == hrow1[x] and placement[1] == hrow9[0]:
										hrow9[x] = "_"
										frow9[x] = "_"
										fcounter -= 1
										makehboard()
									if placement[0] == hrow1[x] and placement[1] == hrow10[0]:
										hrow10[x] = "_"
										frow10[x] = "_"
										fcounter -= 1
										makehboard()
									if placement[0] == hrow1[x] and placement[1] == hrow11[0]:
										hrow11[x] = "_"
										frow11[x] = "_"
										fcounter -= 1
										makehboard()
			elif choice == "r":
				reveal = input("Which spot would you like to reveal? Type in the column number first and then the row number, space in between: ")
				rplace = reveal.split()
				for x in range(11):
					if rplace[0] == hrow1[x] and rplace[1] == hrow2[0] and hrow2[x] != "F":
						if row2[x] == "*":
							hrow2[x] = "*"
							makehboard()
							print("You lose!")
							gamestate = "done"
							break
						elif row2[x] == "_":
							hrow2[x] = "R"
							makehboard()
						elif row2[x] == "1":
							hrow2[x] = "1"
							makehboard()
						elif row2[x] == "2":
							hrow2[x] = "2"
							makehboard()
						elif row2[x] == "3":
							hrow2[x] = "3"
							makehboard()
					if rplace[0] == row1[x] and rplace[1] == row3[0] and row3[x] != "F":
						if row3[x] == "*":
							hrow3[x] = "*"
							makehboard()
							print("You lose!")
							gamestate = "done"
							break
						elif row3[x] == "_":
							hrow3[x] = "R"
							makehboard()
						elif row3[x] == "1":
							hrow3[x] = "1"
							makehboard()
						elif row3[x] == "2":
							hrow2[x] = "2"
							makehboard()
						elif row3[x] == "3":
							hrow3[x] = "3"
							makehboard()
					if rplace[0] == row1[x] and rplace[1] == row4[0] and row4[x] != "F":
						if row4[x] == "*":
							hrow4[x] = "*"
							makehboard()
							print("You lose!")
							gamestate = "done"
							break
						elif row4[x] == "_":
							hrow4[x] = "R"
							makehboard()
						elif row4[x] == "1":
							hrow4[x] = "1"
							makehboard()
						elif row4[x] == "2":
							hrow4[x] = "2"
							makehboard()
						elif row4[x] == "3":
							hrow4[x] = "3"
							makehboard()
					if rplace[0] == row1[x] and rplace[1] == row5[0] and row5[x] != "F":
						if row5[x] == "*":
							hrow5[x] = "*"
							makehboard()
							print("You lose!")
							gamestate = "done"
							break
						elif row5[x] == "_":
							hrow5[x] = "R"
							makehboard()
						elif row5[x] == "1":
							hrow5[x] = "1"
							makehboard()
						elif row5[x] == "2":
							hrow5[x] = "2"
							makehboard()
						elif row5[x] == "3":
							hrow5[x] = "3"
							makehboard()
					if rplace[0] == row1[x] and rplace[1] == row6[0] and row6[x] != "F":
						if row6[x] == "*":
							hrow6[x] = "*"
							makehboard()
							print("You lose!")
							gamestate = "done"
							break
						elif row6[x] == "_":
							hrow6[x] = "R"
							makehboard()
						elif row6[x] == "1":
							hrow6[x] = "1"
							makehboard()
						elif row6[x] == "2":
							hrow6[x] = "2"
							makehboard()
						elif row6[x] == "3":
							hrow6[x] = "3"
							makehboard()
					if rplace[0] == row1[x] and rplace[1] == row7[0] and row7[x] != "F":
						if row7[x] == "*":
							hrow7[x] = "*"
							makehboard()
							print("You lose!")
							gamestate = "done"
							break
						elif row7[x] == "_":
							hrow7[x] = "R"
							makehboard()
						elif row7[x] == "1":
							hrow7[x] = "1"
							makehboard()
						elif row7[x] == "2":
							hrow7[x] = "2"
							makehboard()
						elif row7[x] == "3":
							hrow7[x] = "3"
							makehboard()
					if rplace[0] == row1[x] and rplace[1] == row8[0] and row8[x] != "F":
						if row8[x] == "*":
							hrow8[x] = "*"
							makehboard()
							print("You lose!")
							gamestate = "done"
							break
						elif row8[x] == "_":
							hrow8[x] = "R"
							makehboard()
						elif row8[x] == "1":
							hrow8[x] = "1"
							makehboard()
						elif row8[x] == "2":
							hrow8[x] = "2"
							makehboard()
						elif row8[x] == "3":
							hrow8[x] = "3"
							makehboard()
					if rplace[0] == row1[x] and rplace[1] == row9[0] and row9[x] != "F":
						if row9[x] == "*":
							hrow9[x] = "*"
							makehboard()
							print("You lose!")
							gamestate = "done"
							break
						elif row9[x] == "_":
							hrow9[x] = "R"
							makehboard()
						elif row9[x] == "1":
							hrow2[x] = "1"
							makehboard()
						elif row9[x] == "2":
							hrow2[x] = "2"
							makehboard()
						elif row9[x] == "3":
							hrow9[x] = "3"
							makehboard()
					if rplace[0] == row1[x] and rplace[1] == row10[0] and row10[x] != "F":
						if row10[x] == "*":
							hrow10[x] = "*"
							makehboard()
							print("You lose!")
							gamestate = "done"
							break
						elif row10[x] == "_":
							hrow10[x] = "R"
							makehboard()
						elif row10[x] == "1":
							hrow10[x] = "1"
							makehboard()
						elif row10[x] == "2":
							hrow10[x] = "2"
							makehboard()
						elif row10[x] == "3":
							hrow10[x] = "3"
							makehboard()
					if rplace[0] == row1[x] and rplace[1] == row11[0] and row11[x] != "F":
						if row11[x] == "*":
							hrow11[x] = "*"
							makehboard()
							print("You lose!")
							gamestate = "done"
							break
						elif row11[x] == "_":
							hrow11[x] = "R"
							makehboard()
						elif row11[x] == "1":
							hrow11[x] = "1"
							makehboard()
						elif row11[x] == "2":
							hrow11[x] = "2"
							makehboard()
						elif row11[x] == "3":
							hrow11[x] = "3"
							makehboard()
						
gameloop()


