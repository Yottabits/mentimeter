import requests
import json

url = 'https://govote.at/questions'

# Data to POST
payload = {#'utf8': '',
        #'authenticity_token': '',
        'code': 'e6f3b0',
        #'multiple_votes': '',
        #'series_key': '',
        #'series_last':'',
        #'series_index': '',
        'vote': '1258550'
        }

# Headers
headers = {
        'Host': 'www.govote.at',
        #'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0',
        #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        #'Accept-Language': 'en-US,en;q=0.5',
        #'Accept-Encoding': 'gzip, deflate',
        }

# Cookies
cookies = dict(ct='0')

r = requests.post(url, data=payload, headers=headers, cookies=cookies)
print(r.status_code)
print(r.headers)
print(r.text)
