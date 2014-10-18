from twilio.rest import TwilioRestClient 
import getpass
import json
import signal, os

account = "AC5bc10b06dfef6a0d19cfef184406cd74" 
token = "c7fb839a2ebd320b392654eaa01cb22a"
client = TwilioRestClient(account, token)

j = json.loads(open('card.json').read())
locked = True
status = 'closed'
while True:
	card = getpass.getpass('Swipe Card: ')
	extra = getpass.getpass('')
	
	card = card[:18]
	card = filter(str.isdigit, card)
	if card not in j:
		print 'Get outta here!'
		message = client.messages.create(to="+16309950526", from_="+13313056100",body= "id: " + card + " tried to use the lock")
	else:
		if locked:
			locked = False
			status = 'opened'		
		else:
			locked = True
			status = 'closed'
		print 'Access Granted'
		message = client.messages.create(to="+16309950526", from_="+13313056100",body= j[card] + " " + status + "  the lock")
