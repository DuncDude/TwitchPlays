
#python file reads the contents of a file and then deletes it
from pynput.keyboard import Key, Controller
keyboard = Controller()

import time
import os
import subprocess
amount =0
#time of delay for keystrokes
with open('settings.txt', 'r') as file:
	data = file.readlines()
	amount = data[9]
	amount = (float(amount)/10)
#amount = float(amount)
#amount = (int(amount)/10)



#list of keys mappings arrays
maps = ["a","b","x","y","up","down","left","right","enter","c","l","r"]
file1 = open('settings.txt', 'r') 
Lines = file1.readlines() 
direct = Lines[19].strip('\n')


#Pause Function
def Pause():
	pase = raw_input("Press Enter.. ")
	return

def Banner():
	#clearscreen
	os.system('cls' if os.name == 'nt' else 'clear')
	
	global amount
	#print title
	print("___________       .__  __         .__   __________.__                       ")
	print("\__    ___/_  _  _|__|/  |_  ____ |  |__\______   \  | _____  ___.__. ______")
	print("  |    |  \ \/ \/ /  \   __\/ ___\|  |  \|     ___/  | \__  \<   |  |/  ___/")
	print("  |    |   \     /|  ||  | \  \___|   Y  \    |   |  |__/ __ \\___  |\___ \ ")
	print("  |____|    \/\_/ |__||__|  \___  >___|  /____|   |____(____  / ____/____  >")
	print("                                \/     \/                   \/\/         \/ ")
	print("----------------------------------------------------------------------------")
	#amount =raw_input("Some games have differnt response times to length of key press enter the time in milliseconds(.2): ")
	return

#map keys to file settings.txt
def map():
	Banner()
	print("Mapping keys to settings.txt file (default values will be used if file has not been edited")
	i = 0
	x=32
	global maps
	while x <= 45:
		with open('settings.txt', 'r') as file:
			data = file.readlines()
		#print(data)
# now change the 2nd line, note that you have to add a newline
		print("Maps location " + str(i))
		print("line location " + str(x))
		print("Current chat command " + (data[x-1]) + " set to the " + data[x] + " key.")
		maps[i] = data[x]
		maps[i] = maps[i].strip('\n')
		maps[i] = maps[i].strip('\t')
		x += 2
		i +=1
	#Pause()
	return

def wasd():
	global amount
	global maps

	map()
	Banner()
	print("Started Stream WASD")
	print("KeyPress down time is : " + str(amount) + " seconds")
	while True:
		try:
			f = open("file.txt", "r")
			letter = f.read()
			print("Letter recieved: " + letter)
			if letter == "U":
				print("command UP recognized! ")
				#print(W emulated)
				keyboard.press('w')
				time.sleep(amount)
				keyboard.release('w')
			if letter == "D":
				print("command DOWN recognized! ")
				keyboard.press('s')
				time.sleep(amount)
				keyboard.release('s')
			if letter == "L":
				print("command LEFT recognized! ")
				keyboard.press('a')
				time.sleep(amount)
				keyboard.release('a')
			if letter == "R":
				print("command RIGHT recognized! ")
				keyboard.press('d')
				time.sleep(amount)
				keyboard.release('d')
			if letter == "S":
				print("command START recognized! ")
				keyboard.press(Key.enter)
				time.sleep(amount)
				keyboard.release(Key.enter)
			if letter == "A":
				print("command A recognized! ")
				keyboard.press(maps[0])
				time.sleep(amount)
				keyboard.release(maps[0])
			if letter == "B":
				print("command B recognized! ")
				keyboard.press(maps[1])
				time.sleep(amount)
				keyboard.release(maps[1])
			if letter == "X":
				print("command X recognized! ")
				keyboard.press(maps[2])
				time.sleep(amount)
				keyboard.release(maps[2])
			if letter == "Y":
				print("command Y recognized! ")
				keyboard.press(maps[3])
				time.sleep(amount)
				keyboard.release(maps[3])
			if letter == "r1":
				print("command r1 recognized! ")
				keyboard.press(maps[4])
				time.sleep(amount)
				keyboard.release(maps[4])
			if letter == "l":
				print("command l1 recognized! ")
				keyboard.press(maps[5])
				time.sleep(amount)
				keyboard.release(maps[5])
			if letter == "C":
				print("command SELECT recognized! ")
				keyboard.press(maps[6])
				time.sleep(amount)
				keyboard.release(maps[6])
			if letter =="" :
				print("SOmething went wrong")
		
			#Delte file
			 
		except:
			#rint("something there")
			pass
		try:
			os.remove("file.txt")
		except:
			pass
		time.sleep(.1)

def arrow():
	global amount
	global maps
	map()
	Banner()
	print("Started Stream Arrows")
	print("KeyPress down time is : " + str(amount)+ " seconds")
	while True:
		try:
			f = open("file.txt", "r")
			letter = f.read()
			print("Letter recieved: " + letter)
			if letter == "U":
				print("command UP recognized! ")
				#print(maps[0])
				keyboard.press(Key.up)
				time.sleep(amount)
				keyboard.release(Key.up)
			if letter == "D":
				print("command DOWN recognized! ")
				keyboard.press(Key.down)
				time.sleep(amount)
				keyboard.release(Key.down)
			if letter == "L":
				print("command LEFT recognized! ")
				keyboard.press(Key.left)
				time.sleep(amount)
				keyboard.release(Key.left)
			if letter == "R":
				print("command RIGHT recognized! ")
				keyboard.press(Key.right)
				time.sleep(amount)
				keyboard.release(Key.right)
			if letter == "S":
				print("command START recognized! ")
				keyboard.press(Key.enter)
				time.sleep(amount)
				keyboard.release(Key.enter)
			if letter == "A":
				print("command A recognized! ")
				keyboard.press(maps[0])
				time.sleep(amount)
				keyboard.release(maps[0])
			if letter == "B":
				print("command B recognized! ")
				keyboard.press(maps[1])
				time.sleep(amount)
				keyboard.release(maps[1])
			if letter == "X":
				print("command X recognized! ")
				keyboard.press(maps[2])
				time.sleep(amount)
				keyboard.release(maps[2])
			if letter == "Y":
				print("command Y recognized! ")
				keyboard.press(maps[3])
				time.sleep(amount)
				keyboard.release(maps[3])
			if letter == "r1":
				print("command r1 recognized! ")
				keyboard.press(maps[4])
				time.sleep(amount)
				keyboard.release(maps[4])
			if letter == "l":
				print("command l1 recognized! ")
				keyboard.press(maps[5])
				time.sleep(amount)
				keyboard.release(maps[5])
			if letter == "C":
				print("command SELECT recognized! ")
				keyboard.press(maps[6])
				time.sleep(amount)
				keyboard.release(maps[6])
			if letter =="" :
				print("SOmething went wrong")
		
			#Delte file
			 
		except:
			#rint("something there")
			pass
		try:
			os.remove("file.txt")
		except:
			pass
		time.sleep(.1)
print(direct)
if direct == "arrows":
	arrow()
if direct == "wasd":
	wasd()