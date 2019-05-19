import requests

#{"ip":"115.205.235.10","locale":""}
url = 'http://ip.hahado.cn/ip'
proxy = {'http':'http://H076RR7P08B5W86P:D6B83B693E9016A2@http-pro.abuyun.com:9010'}
response = requests.get(url=url, proxies=proxy)

print(response.text)