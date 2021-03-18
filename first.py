import requests
 
r = requests.get('https://google.com')
 
if r.status_code == 200:
    print('OK!')
 
if r.status_code == 404:
    print('Not found')
