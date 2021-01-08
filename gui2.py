#!/usr/bin/env python2

import os
import Tkinter as tk
root = tk.Tk()
root.geometry("600x500")
#Title the window
root.title("Twitch Plays Key Emulator v1.2")
# Tkinter string variable 

 

def run():
	os.system("./test.sh ")

def leave():\
	#kill all python and node running
	os.system("killall -9 node && killall -9 python")
	exit()
	
	
#clears all the text inputs
def clear():
	textbox2.delete("1.0","end")
	textbox.delete("1.0","end")
	Account.delete("1.0","end")
	OAUTH.delete("1.0","end")
	Channel.delete("1.0","end")
	delay.delete(0,"end")
	return

#hnadles the radio button functions
def arrows():
	with open('settings.txt', 'r') as file:
		data = file.readlines()
		#print(data)
# now change the 2nd line, note that you have to add a newline
		
	data[19] = "arrows" + '\n'
	with open('settings.txt', 'w') as file:
   		file.writelines( data )
	print("Changed to Arrows")
	return


def wasd():
	with open('settings.txt', 'r') as file:
		data = file.readlines()
		#print(data)
# now change the 2nd line, note that you have to add a newline
		
	data[19] = "wasd" + '\n'
	with open('settings.txt', 'w') as file:
   		file.writelines( data )
	print("Changed to WASD")
	return
	
	
	
#get text input from the text boxes ands set the readme file to the new values
def getTextInput():
	result=textbox2.get("1.0","end")
	#strip of new lines
	result = result.replace('\n','')
	print(result)
	i = 0
	x=32
	while x <= 45:
		with open('settings.txt', 'r') as file:
			data = file.readlines()
		#print(data)
# now change the 2nd line, note that you have to add a newline
		print("Current chat command " + (data[x-1]) + " Changing  to the " + result[i] + " key.")
		data[x] = result[i] + '\n'
		with open('settings.txt', 'w') as file:
   			file.writelines( data )
		x += 2
		i +=1
		
	#replaces the CR.js values with the ones from the gui
	tw=Account.get("1.0","end")
	oa=OAUTH.get("1.0","end")
	ch=Channel.get("1.0","end")

	#strip of new lines
	tw = tw.replace('\n','')
	oa = oa.replace('\n','')
	ch = ch.replace('\n','')
	#print("Adding " + result)
	usr = 13
	oauth= 16
	chan= 19
	with open('CR.js', 'r') as file:
		data = file.readlines()
		data[usr] = tw + '\n'
		data[oauth] = oa + '\n'
		data[chan] = ch + '\n'
		with open('CR.js', 'w') as file:
   			file.writelines( data )
			
	#load up teh spinbox amount
	timer = delay.get()
	print("Delay: " + str(timer))
	with open('settings.txt', 'r') as file:
		data = file.readlines()
		timer = timer.replace('\n','')
		data[9] = timer+ '\n'
	with open('settings.txt', 'w') as file:
   		file.writelines( data )

	
	#reload readme

	list()




	


#read corntrolls  from file
def list():	
	#allow changes to the left textbox
	textbox.configure(state='normal')
	#clear the text boxes
	clear()
	x=32
	while x <= 46:
		with open('settings.txt', 'r') as file:
			data = file.readlines()
			theFile = data
			
		#print(data)
# now change the 2nd line, note that you have to add a newline
		print("Current chat command " + (data[x-1]) + " set to the " + data[x] + " key.")
	#insert each line in to the textbox
		textbox2.insert(tk.END, data[x])
		textbox.insert(tk.END, data[x-1])
		x += 2
		
		
	#READ THE CHATREADER FILE AND PULL INFO
	usr = 13
	oauth= 16
	chan= 19
	with open('CR.js', 'r') as file:
		data = file.readlines()
		#print(data)
# now change the 2nd line, note that you have to add a newline
		print("Current Twitch Account " + (data[usr]) + " The account (username) that the chatbot uses to send chat messages. This can be your Twitch account. Alternately, many developers choose to create a second Twitch account for their bot, so it's clear from whom the messages originate.") 
		Account.insert(tk.END, data[usr])

		print("Current OAUTH_TOKEN " + (data[oauth]) + " The token to authenticate your chatbot with Twitch's servers. Generate this with https://twitchapps.com/tmi/ (a Twitch community-driven wrapper around the Twitch API), while logged in to your account. The token will be an alphanumeric string." )
		OAUTH.insert(tk.END, data[oauth])
		print("Current Twitch Channel " + (data[chan]) + " The Twitch channel name where you want to run the bot. Usually this is your main Twitch account.")
		Channel.insert(tk.END, data[chan])
	
	
	with open('settings.txt', 'r') as file:
		data = file.readlines()
		
		delay.insert(tk.END, data[9].replace('\n',''))
	
	#disable changing of values
	textbox.configure(state='disabled')
		
	
		#print(data[42])
		




	
#create the buttons and boxes#########################
#Labels
header = tk.Label(root, text = " ")
label1 = tk.Label(root, text = "Twitch Chat Input",font = 'bold')
label2 = tk.Label(root, text = "Keys Emulated",font = 'bold')
label3 = tk.Label(root, text = "Twitch Account")
label4 = tk.Label(root, text = "OAUTH Token")
label5 = tk.Label(root, text = "Channel being followed")
label6 = tk.Label(root, text = "Directional input to KeyBoard output",font = 'bold')
label7 = tk.Label(root, text = "!start always set to 'Enter' key", font=("Courier", 8))
label8 = tk.Label(root, text = "Keypress time in miliseconds",font = 'bold')
label9 = tk.Label(root, text = "Directional input: !up !down !left !right",font = ("Courier", 8))



#text boxes
textbox = tk.Text(root, height=8, width = 10, font=("Helvetica", 20))
textbox2 = tk.Text(root, height=8, width = 5, font=("Helvetica", 20))
Account = tk.Text(root, height=1, width = 35)
OAUTH = tk.Text(root, height=1, width = 35)
Channel = tk.Text(root, height=1, width = 35)

#buttons
btnRead = tk.Button(root, height=1, width=30, text="Save Settings", command=getTextInput)
btnRead2 = tk.Button(root, height=1, width=30, text="Load Settings", command=list)
btnRead3 = tk.Button(root, height=1, width=30, text="Run Bot", command=run)
btnRead4 = tk.Button(root, height=1, width=30, text="Exit/Stop Bot", command=leave)

#radio Buttons
radio1 = tk.Radiobutton(root, text="WASD", value=1, command = wasd)
radio2 = tk.Radiobutton(root, text="Arrow keys", value=2, command = arrows)

#SpinBox
delay = tk.Spinbox(root, from_ = 0, to = 10)




#place things on canvas#######################################
header.grid(row = 0, column = 0)

#top text box label
label3.grid(row = 2, column = 0)
label4.grid(row = 3, column = 0)
label5.grid(row = 4, column = 0)

#text boxes
Account.grid(row = 2, column = 1)
OAUTH.grid(row = 3,column = 1)
Channel.grid(row = 4,column = 1)
#space
header.grid(row = 5, column = 0)

#labels
label1.grid(row = 6, column = 0)
label2.grid(row = 6, column = 1)

textbox.grid(row = 7, column = 0)
textbox2.grid(row = 7,column = 1)

#spacer
header.grid(row = 8, column = 0)

#small text
label9.grid(row = 8, column = 0)
label7.grid(row = 8, column = 1)

#spinBox delay
label8.grid(row = 9, column = 1)
delay.grid(row = 10, column = 1)

#radio
label6.grid(row = 9, column = 0)
radio1.grid(row = 10, column = 0)
radio2.grid(row = 11, column = 0)


#buttons
btnRead.grid(row = 12,column = 1)
btnRead2.grid(row = 12,column = 0)



btnRead3.grid(row = 13,column = 1)			  
btnRead4.grid(row = 13,column = 0)		  
root.mainloop()
