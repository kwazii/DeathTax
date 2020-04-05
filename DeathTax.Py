import random
def roll():
	value = random.randrange(1,7)
	if value == 1:
		print(f"Do {random.randrange(12,24)} PushUps fatass")
	elif value == 2:
		print(f"Do {random.randrange(10,18)} Burpees fatass")
	elif value == 3:
		print(f"Do {random.randrange(12,20)} Lunges fatass")
	elif value == 4:
		print(f"Do {random.randrange(15,25)} Squats fatass")
	elif value == 5:
		print(f"Do {random.randrange(15,20)} Crunches fatass")
	else:
		print(f"Do {random.randrange(20,45)} Planks fatass")
try:
	while True:
		userInp = input("Do you want to roll?")
		if userInp == "n":
			break
		roll()	
except Exception as e:
	print(e)
	input()
