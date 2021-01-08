//TO run this bot in cli type node botPython.js
//resource https://dev.twitch.tv/docs/irc





const tmi = require('tmi.js');

// Define configuration options
const opts = {
  identity: {
    username: 
"K_Stew_Anonymous"
	  ,
    password: 
"https://twitchapps.com/tmi/"
  },
  channels: [
"K_Stew_Anonymous"
  ]
};

// Create a client with our options
const client = new tmi.client(opts);

// Register our event handlers (defined below)
client.on('message', onMessageHandler);
client.on('connected', onConnectedHandler);

// Connect to Twitch:
client.connect();

// Called every time a message comes in
function onMessageHandler (target, context, msg, self) {
  if (self) { return; } // Ignore messages from the bot

  // Remove whitespace from chat message
  const commandName = msg.trim();

  // If the command is known, let's execute it
  if (commandName === '!up') {
    client.say(target, `Command Accepted`);

	var fs = require('fs');
	fs.writeFile('file.txt', 'U', function (err) {
	if (err) throw err;
	console.log('File.txt Updated!');
	}); ; 

  }

  if (commandName === '!down') {;
    client.say(target, `Command Accepted`);

	var fs = require('fs');
	fs.writeFile('file.txt', 'D', function (err) {
	if (err) throw err;
	console.log('File.txt Updated!');
	}); ; 

  }
	
  if (commandName === '!left') {
    client.say(target, `Command Accepted`);

	var fs = require('fs');
	fs.writeFile('file.txt', 'L', function (err) {
	if (err) throw err;
	console.log('File.txt Updated!');
	}); ; 

  }
	  
  if (commandName === '!right') {
    client.say(target, `Command Accepted`);

	var fs = require('fs');
	fs.writeFile('file.txt', 'R', function (err) {
	if (err) throw err;
	console.log('File.txt Updated!');
	}); ; 
 
  }
	
	
  if (commandName === '!start') {
    client.say(target, `Command Accepted`);

	var fs = require('fs');
	fs.writeFile('file.txt', 'S', function (err) {
	if (err) throw err;
	console.log('File.txt Updated!');
	}); ; 

  }
	
  if (commandName === '!a') {
    client.say(target, `Command Accepted`);

	var fs = require('fs');
	fs.writeFile('file.txt', 'A', function (err) {
	if (err) throw err;
	console.log('File.txt Updated!');
	}); ; 

  }
	
  if (commandName === '!b') {
    client.say(target, `Command Accepted`);

	var fs = require('fs');
	fs.writeFile('file.txt', 'B', function (err) {
	if (err) throw err;
	console.log('File.txt Updated!');
	}); ; 

  }
	
  if (commandName === '!x') {
    client.say(target, `Command Accepted`);

	var fs = require('fs');
	fs.writeFile('file.txt', 'X', function (err) {
	if (err) throw err;
	console.log('File.txt Updated!');
	}); ; 

  }
	
  if (commandName === '!y') {
    client.say(target, `Command Accepted`);

	var fs = require('fs');
	fs.writeFile('file.txt', 'Y', function (err) {
	if (err) throw err;
	console.log('File.txt Updated!');
	}); ; 

  }

  if (commandName === '!l1') {
    client.say(target, `Command Accepted`);

	var fs = require('fs');
	fs.writeFile('file.txt', 'l1', function (err) {
	if (err) throw err;
	console.log('File.txt Updated!');
	}); ; 

  }

  if (commandName === '!r1') {
    client.say(target, `Command Accepted`);

	var fs = require('fs');
	fs.writeFile('file.txt', 'r1', function (err) {
	if (err) throw err;
	console.log('File.txt Updated!');
	}); ; 

  }

  if (commandName === '!select') {;
    client.say(target, `Command Accepted`);

	var fs = require('fs');
	fs.writeFile('file.txt', 'C', function (err) {
	if (err) throw err;
	console.log('File.txt Updated!');
	}); ; 

    console.log(`* Chat User Input: ${commandName}`);
  } else {
    console.log(`* Chat User Input: ${commandName}`);
  }





//END OF FUNCTIOM FOR THE THING
}


// Called every time the bot connects to Twitch chat
function onConnectedHandler (addr, port) {
  console.log(`* Connected to ${addr}:${port}`);
}
