"""
python uguestPSKChange.py --newpass xxxxx 
"""
import requests
import sys
import json
#payload  = raw_input("Please provide new password at least 8 Char long")

def newPSK(nid, newPSK1):
   payload = "{\"psk\": \"" + str(newPSK1) +"\"}"
   url = "https://dashboard.meraki.com/api/v0/networks/%(nid)s/ssids/1" % {'nid':nid}

   headers = {
            'x-cisco-meraki-api-key': "{{API_Key}}",
            'content-type': "application/json",
            'cache-control': "no-cache",

            }

   response = requests.request("PUT",url,data=payload,headers=headers)
   #raw_response = response.text

   #parsed_response = json.loads(raw_response)


if __name__ == "__main__":

    newPSK1  = raw_input("Please provide new password at least 8 Char long:")
    print newPSK1
    newPSK('{{test_network_Id', newPSK1)

