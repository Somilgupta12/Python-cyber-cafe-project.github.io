import random
def compmov():
	while True:
		q=random.randint(1,9)
		if q not in d and q not in e:
			break
	return q
def board():
	print()
	print()
	for j in (a,b,c):
		alpha=""
		for i in j:
			alpha+=str(i)+" |"
		print(alpha[:-1])
		if j==c:
			break
		print("__|__|__")
	print(" | | ")
	print()
def game_ends():
	global jas
	for i in jas:
		if d&i==i:
			print()
			print(Player1+" wins")
			return False
		elif e&i==i:
			print()
			print(Player2+" wins")
			return False
	return True
def change(f,g):
	global a,b,c
	if f in a:
		a[a.index(f)]=g
	elif f in b:
		b[b.index(f)]=g
	elif f in c:
		c[c.index(f)]=g
	else:
		print()
		print("ERROR!!!")
		print()
		print("You need to restart the game.")
		exit()
Playername=input("\nEnter your name:")
jas=winning_combinations=({1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},
{1,5,9},{3,5,7})
while True:
	a=[1,2,3]
	b=[4,5,6]
	c=[7,8,9]
	d=set()
	e=set()
	pn=1#Player now

	gam=input(("\nWant to take X or O:"))

	if gam in "Xx":
		Player1=Playername
		Player2="Computer"
		print("\nComputer:Here is board")
		board()

		while game_ends():
			count=0
			for i in a+b+c:
				if i=="X" or i=="O":
					count+=1
				if count==9:
					print("\nDRAW!!")
					break

				if pn==1:
					print()
					q1=int(input(Player1+", Where do you want X:"))
					d.add(q1)
					change(q1,"X")
					pn=2
				else:
					q=compmov()
					print("Computer played at",q)
					e.add(q)
					change(q,"O")
					pn=1
					board()
	elif gam in "Oo":
		Player1="Computer"
		Player2=Playername
		print("Computer:Here is board")
		board()
		while game_ends():
			count=0
			for i in a+b+c:
				if i=="X" or i=="O":
					count+=1
			if count==9:
				print("\nDRAW!!")
				break

			if pn==1:
				q=compmov()
				print("Computer played at",q)
				d.add(q)
				change(q,"X")
				pn=2
				board()
			else:
				print()
				q1=int(input(Player2+",Where do you want O:"))
				e.add(q1)
				change(q1,"O")
				pn=1
		else:
			print("\nERROR!!!")
			print("\nYou need to restart the game.")
			exit()

		fgh=input("\nPress N to stop")
		if fgh in "Nn":
			print("Quitting from the game...")
			break
