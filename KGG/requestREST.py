import requests



def materialise(file):
    # URLS
    url_post = "https://kgg.openmetrics.eu/upload"
    url_get = "https://kgg.openmetrics.eu/download"

    # GET FILE

    files=[
        ('file',(file+'.ifc',open(file, 'rb'),'application/octet-stream'))
    ]

    payload = {}

    s = requests.Session()
    s.get('https://kgg.openmetrics.eu/')

    headers_post = {
    'Cookie': 'JSESSIONID=' + s.cookies.get_dict()['JSESSIONID']
    }

    headers_get = {
    'Cookie': 'JSESSIONID=' + s.cookies.get_dict()['JSESSIONID']
    }

    response_post = requests.request("POST", url_post, headers=headers_post, data=payload, files=files)
    response_get = requests.request("GET", url_get, headers=headers_get, data=payload)

    return response_get.text