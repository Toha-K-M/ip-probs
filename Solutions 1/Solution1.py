import requests

api = "http://ip-api.com/json/"
ans = ''
infos = []

def get(ip):
    query = api + ip
    json_data = requests.get(query).json()
    infos.append(json_data['city']+', '+json_data['regionName']+' ('+json_data['country']+')')
    json_data=None

while True:
    try:
        print("Enter an IP: ")
        ip = input()
        get(ip)
    except:
        print("Sorry, Wrong Input. Please enter an ip address")
        continue
    else:
        while ans not in('y','n'):
            print("Enter another IP? y/n")
            ans = input()
        if(ans is 'n'):
            break
        else:
            ans = ""
            continue
# ip = "63.70.164.200"
for info in infos:
    print(info)
