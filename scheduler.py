import requests
import os


body = 'Below are the slots available '
date = '04-06-2021'
district = '196'
counter = 0
result = os.popen("curl -X GET \"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=" + district + "&date=" + date +"\" -H \"accept: application/json\" -H \"Accept-Language: hi_IN\" ").read()
# print(result)

centers = json.loads( result )['sessions']

res = list( filter( lambda x: x['min_age_limit']==18 and (x['available_capacity_dose1'] > 0 or x['available_capacity_dose2'] > 0 or x['available_capacity'] > 0 ), centers ) )

body = body + str( res )

from twilio.rest import Client 
 
account_sid = 'ACe71268fac28426afe2e8b3111427044c' 
auth_token = '225e7917f69bc43a420ba69a47270ac7' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body=body,      
                              to='whatsapp:+918600044990' 
                          ) 
 
# print(message.sid)
