import requests
import json
import logging
import asyncio

logging.basicConfig(filename='result.log', format='%(asctime)s ^ %(message)s', level=logging.INFO)
user_input = str(input('Hello, please point to path of text file: '))

with open(user_input) as in_file:
    values = in_file.readlines()
    ip_list = []
    for i in values:
        # convert to list
        records = i.split()
        # if values not equal an ip address, don't add them to list
        if records[0] != 'src-ip-addr':
            ip_list.append(records[0])
    print('in process.. ')
    ip_list

async def abuseipdb(list):

    # check if ips are unique
    unique_ips = set(list)
    amount_ip = len(unique_ips)

    # try except block to catch user's error inputs
    for address in unique_ips:
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

        # variables for 'if', 'else' statements
        abuse_confidence = decode_response['data']['abuseConfidenceScore']
        total_reports = decode_response['data']['totalReports']
        is_public = decode_response['data']['isp']
        ip = decode_response['data']['ipAddress']

        # in a case if user entered private address space
        if is_public == "Private IP Address LAN":
            print(f"ANSWER FROM: www.abuseipdb.com\nthis ip [ {ip} ] in private address space,\nso, there is no point to check it")

        # if abuse confidence or total reports is higher than 2, counts ip as compromised, otherwise it's 'clear'
        elif abuse_confidence > 2 or total_reports > 2:
            amount_ip = amount_ip - 1
            answer_compromised = f"ANSWER FROM: www.abuseipdb.com\nTHIS IP [ {ip} ] IS PROBABLY COMPROMISED\n{json.dumps(decode_response, sort_keys=True, indent=1)}"
            # save requested ip in a log file
            logging.info(answer_compromised)

        else:
            # in a case if address is clear
            answer_clear = f"ANSWER FROM: www.abuseipdb.com\nTHIS IP [ {ip} ] IS CLEAR\n{json.dumps(decode_response, sort_keys=True, indent=1)}"
            logging.info(answer_clear)


    # statistics
    uniq_amount_ip = len(unique_ips)
    compromised_ip = uniq_amount_ip-amount_ip
    result = (f"total amount of address [{uniq_amount_ip}] from them [{amount_ip}] CLEAR, and [{compromised_ip}] are COMPROMISED")
    logging.info(result)
    print(result)

async def main():
    task1 = asyncio.create_task(abuseipdb(ip_list))

    await task1

asyncio.run(main())