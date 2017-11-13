import requests
import json


def getpushFW(nid):
   url = "https://dashboard.meraki.com/api/v0/networks/%(nid)s/l3FirewallRules" % {'nid': nid}
   # Central Repository for FW rules
   fname = "MerakiMXL3Rules.json"

   with open(fname) as f:
	raw_payload = f.read()
	
   # Check json is valid
   try:
	json.loads(raw_payload)
   except ValueError as e:
	raise Exception('JSON File %s is Invalid! %s' % (fname, e))
   headers = {
    'x-cisco-meraki-api-key': "{{API_Key}}",
    'content-type': "application/json",
    'cache-control': "no-cache",
    
       }

   response = requests.request("PUT", url, data=raw_payload, headers=headers)

   print json.dumps(json.loads(response.text), indent=2)

if __name__ == "__main__":
   getpushFW('{{test_NetworkID}}')

