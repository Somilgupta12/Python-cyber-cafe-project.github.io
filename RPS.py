import random as r
draw=[1,1],[2,2],[3,3]
win=[1,3],[2,1],[3,2]
lose=[3,1],[1,2],[2,3]
d={1:"Rock",2:"Paper",3:"Scissor"}
total_win=total_lose=total_draw=0
while True:
	b=r.randint(1,3)
	a=int(input("\n1.Rock\n2.Paper\n3.Scissor\n"))
	c=[a,b]
	print("\nYou played",d[a])
	print("Computer played",d[b])
	print()
	if c in draw:
		print("Draw")	
		total_draw+=1
	if c in win:
		print("You win.")
		total_win+=1
	if c in lose:
		print("Computer wins.")
		total_lose+=1
	q=input("Do you want to continue Y/N:")
	if q in "Nn":
		print("Total wins =",total_win)
		print("Total loses =",total_lose)
		print("Total draws =",total_draw)
		print("See you again. BYE!")
		break
	else:
		print("\nPlaying again.....")
