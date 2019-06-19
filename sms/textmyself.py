#! python3

# DEFINITIONS
account_SID = ''
auth_token = ''
twilio_number = ''
my_number = ''

from twilio.rest import Client

def textmyself(message):
    c = Client(account_SID, auth_token)
    c.messages.create(body=message, from_=twilio_number, to=my_number)


