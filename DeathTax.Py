import random
sPushUps = 0
sBurpees = 0
sLunges = 0
sSquats = 0
sCrunches = 0
sPlanks = 0

def roll():
	global sPushUps, sBurpees, sLunges, sSquats, sCrunches, sPlanks
	value = random.randrange(1,7)
	if value == 1:
		ranroll = random.randrange(12,24)
		sPushUps = sPushUps + ranroll
		print(f"Do {ranroll} PushUps fatass")
	elif value == 2:
		ranroll = random.randrange(10,18)
		sBurpees = sBurpees + ranroll
		print(f"Do {ranroll} Burpees fatass")
	elif value == 3:
		ranroll = random.randrange(12,20)
		sLunges = sLunges + ranroll
		print(f"Do {ranroll} Lunges fatass")
	elif value == 4:
		ranroll = random.randrange(15,25)
		sSquats = sSquats + ranroll
		print(f"Do {ranroll} Squats fatass")
	elif value == 5:
		ranroll = random.randrange(15,20)
		sCrunches = sCrunches + ranroll
		print(f"Do {ranroll} Crunches fatass")
	else:
		ranroll = random.randrange(20,45)
		sPlanks = sPlanks + ranroll
		print(f"Do {ranroll} Planks fatass")
try:
	while True:
		userInp = input("Do you want to roll? \n [Y] Yes [N] No [S] Status \n >>")
		if userInp.upper() == "S":
			print(f"You've Done {sPushUps} PushUps, {sBurpees} Burpees, {sLunges} Lunges, {sSquats} Squats, {sCrunches} Crunches, and {sPlanks} Planks.... FATASS")
			print("\n")
		if userInp.upper() == "Y":
			roll()
			print("\n")
		if userInp.upper() == "N":
			break
		
except Exception as e:
	print(e)
	input()
