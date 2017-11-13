from pushFW import getpushFW
import json
import requests
import csv

#def get_NIDs():
url = "https://dashboard.meraki.com/api/v0/organizations/{{org_id}}/configTemplates"

headers = {
    'x-cisco-meraki-api-key': "{{API_Key}}",
    'content-type': "application/json",
    'cache-control': "no-cache",

    }

response = requests.request("GET", url, headers=headers)
raw_response = response.text

parsed_response = json.loads(raw_response)
#print json.dumps(parsed_response, indent=4)

    #print parsed_response[2]['policy']
    #policies = []
#def get_NIDs(parsed_response):
#NIDs = []
for blck in parsed_response:
	 
            # print blck['policy']
	 if '{{condition_in_name}}' in blck['name']:
	 # from pushFW import getpushFW
        #print blck['id']
	  getpushFW(blck['id'])
