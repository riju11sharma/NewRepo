import os
from twilio.rest import Client

new={
  "keys":
    {
      "sid": "SK99e5d767bfb3723d3ce099dc74fb094c",
      "friendly_name": "User Joey",
      "date_created": "Mon, 13 Jun 2016 22:50:08 +0000",
      "date_updated": "Mon, 13 Jun 2016 22:50:08 +0000"
    },
  "first_page_uri": "/2022-08-12/Accounts/AC3afeffe5b1eedff35d4c3de20c95bfc4/Keys.json?PageSize=50&Page=0",
  "end": 0,
  "previous_page_uri": "/2022-08-12/Accounts/AC3afeffe5b1eedff35d4c3de20c95bfc4/Keys.json?PageSize=50&Page=0",
  "uri": "/2010-04-01/Accounts/AC3afeffe5b1eedff35d4c3de20c95bfc4/Keys.json?PageSize=50&Page=0",
  "page_size": 50,
  "start": 0,
  "next_page_uri": "/2022-08-12/Accounts/AC3afeffe5b1eedff35d4c3de20c95bfc4/Keys.json?PageSize=50&Page=50",
  "page": 0
}
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = [i['sid'] for i in new['keys']]
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

keys = client.keys.list(limit=20)

for record in keys:
    print(record.sid)