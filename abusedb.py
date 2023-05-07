import requests
import json

addr_lst = ['list of ip addresses']



def check_ips(addr_lst):

    uniq_ip = set(addr_lst)
    for address in uniq_ip:

        url = 'https://api.abuseipdb.com/api/v2/check'
        headers = {
            'Accept': 'application/json',
            'Key': 'your api key'
        }

        querystring = {
            'ipAddress': address,
            'maxAgeInDays': '90'
        }

        response = requests.request(method='GET', headers=headers, url=url, params=querystring)
        decode_response = json.loads(response.text)
        abuse_confidence = decode_response['data']['abuseConfidenceScore']
        total_reports = decode_response['data']['totalReports']
        ip = decode_response['data']['ipAddress']

        # if abuse confidence or total reports is higher that 2, ip's is compromised, otherwise shows 'clear'
        if abuse_confidence > 2 or total_reports > 2:
            print(f"THIS IP [{ip}] IS COMPROMISED {json.dumps(decode_response, sort_keys=True, indent=4)}\n")
        else:
            print(f"THIS IP [{ip}] IS CLEAR {json.dumps(decode_response, sort_keys=True, indent=4)}\n" )

if __name__ == "__main__":
    check_ips(addr_lst)
