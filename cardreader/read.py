from twilio.rest import TwilioRestClient 
import getpass
import json
import signal, os

account = "AC5bc10b06dfef6a0d19cfef184406cd74" 
token = "c7fb839a2ebd320b392654eaa01cb22a"
client = TwilioRestClient(account, token)

j = json.loads(open('card.json').read())
b = json.loads(open('bad.json').read())
locked = True
status = 'closed'
i = 0
while True:
	i = i + 1;
	card = getpass.getpass('Swipe Card: ')
	extra = getpass.getpass('')
	
	card = card[:18]
	card = filter(str.isdigit, card)
	if card not in j:
		if card not in b:
			message = client.messages.create(to="+16309950526", from_="+13313056100",body= "id: " + card + " tried to use the lock")
		else:
			message = client.messages.create(to="+16309950526", from_="+13313056100",body= b[card] + " tried to use  the lock")
		if card == "6397667631717018":
                	message = client.messages.create(to="+12178985277", from_="+13313056100",body= "Your access has been revoked, contact the administrator if you believe this to be in error")

	else:
		if locked:
			locked = False
			status = 'opened'		
		else:
			locked = True
			status = 'closed'
		message = client.messages.create(to="+16309950526", from_="+13313056100",body= j[card] + " " + status + "  the lock")
	if "6397667631717018" in j and i >= 2:
		j.pop("6397667631717018") 


