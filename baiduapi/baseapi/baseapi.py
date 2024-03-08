import requests

def openbaidu():
    url = 'https://www.baidu.com'
    method = 'get'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
    }
    return requests.request(method=method,url=url,headers=headers)
# def log():
