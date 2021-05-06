import requests
from requests_toolbelt.utils import dump
from sys import argv

r = requests.get('https://httpbin.org')

data = dump.dump_response(r)
#print(data.decode('utf-8')[18:152])

#18 is where the request method and all ends 
#150 - 152 is where the entire raw request ends

headers = data.decode('utf-8')[18:400]
headers = headers.replace('<', '')
headers = headers.replace('>', '')

#headers = dict([[field.strip() for field in pair.split(':', 1)] for pair in headers.strip().split('\n')])
print(headers)
