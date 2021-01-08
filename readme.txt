#Twitch Plays Key Emulator
Twitch Plays Key Emulator (TPKE) is a program designed to make setups like the infamous TwitchPlayPokemon very easy.
TPKE uses a JS script to read the contents of chat and listen for specfic keywords or commands such as !up, TPKE then using
a Python2 script will emulate keyboard strokes mapped to those commands. The whole think comes in a nice GUI package which
makes it easier for setup espically for the commandline wary.

##Instalation
Go ahead and download the repositry either the .zip or with 'git clone' then using the command line navigate into that
directory. You will see a file called Install.sh, you will need to make this execuctable, do this by typing 'sudo chmod +x Install.sh'
in the command line. After words you will want to run the install script by typing './Install.sh' this may take a minute
if you have trouble with this or errors you can try to manually install the dependcies which are listed below.
'sudo apt-get update'
'sudo apt-get upgrade'
'sudo apt install python2'
'sudo apt install python-pip'
'sudo apt-get install python-tk'
'sudo apt install nodejs'
'sudo apt install npm'
'sudo npm i tmi.js --save'
'sudo pip install pynput'

##Running the Bot
Now that you have all the dependices install you can run the bot by typing 'python gui2.py' in the commmand line. You will shown
a screen with empty text boxes, click the 'load settings' button at the bottom to load the default settings. On the left you will
see a list of commands the users can type in chat, on the right you will see what keys those commands will emulate on you keyboard
NOTE: !start will allways be set to enter, and !up !down etc will always be set to the either wasd or the arrow keys, if you really
want to change these command you can go through the key3.py file. If youd like to change what keywords get picked up you can Change
that in the CR.js file.
At the top you will see a box for your Twitch account, this should be filled in with whatever your twitch login is, MAKE SURE IT IS IN QUOTES
Under the Twitch account you will see a prompt for an OAUTH token, this is a special password twtich uses to let bots login, you can find out what
yours is here https://twitchapps.com/tmi/    MAKE SURE IT IS IN QUOTES
Under the OAUTH box will be a box for the channel whoms chat you wish to follow, this could be anyones channel but you should probaly just use your MAKE SURE IT IS IN QUOTES

Certain games have differnt response for length of keyboard presses, you can change how long a key  board press will last at the bottom right hand
In order to choose weither the bot uses WASD or arrow keys, select one of the radio buttons on the bottom left.
When you have all your settings as you like, Click the 'Save Settings' button and then to start the bot hit 'Run BOt'

## playing a game
Once your bot is running and listeing to chat, you can load up what ever emulator or game you like, as long as that Emulator or
game is selected as your active window, the keyboard emulated strokes should be able to play it

###Have Fun!