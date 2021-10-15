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

    headers_post = {
    'Cookie': 'JSESSIONID=2035B43B86BE40748581C7BECDEE87F1'
    }

    headers_get = {
    'Cookie': 'JSESSIONID=2035B43B86BE40748581C7BECDEE87F1'
    }

    response_post = requests.request("POST", url_post, headers=headers_post, data=payload, files=files)
    response_get = requests.request("GET", url_get, headers=headers_get, data=payload)
    

    return response_get.text