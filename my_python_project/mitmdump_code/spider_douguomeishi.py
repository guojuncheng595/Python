import json

import requests
from multiprocessing import Queue
from handlermongo import mongo_info
from concurrent.futures import ThreadPoolExecutor

# 创建队列
queue_list = Queue()


def handel_request(url, data):

    header = {
        "client": "4",
        "version": "6935.2",
        "device": "MI 5",
        "sdk": "22,5.1.1",
        "imei": "863064010600213",
        "channel": "baidu",
        # "mac": "60:02:B4:C4:B2:D6",
        "resolution": "1280*720",
        "dpi": "1.5",
        # "android-id": "6002b4c4b2d64805",
        # "pseudo-id": "4c4b2d648056002b",
        "brand": "Xiaomi",
        "scale": "1.5",
        "timezone": "28800",
        "language": "zh",
        "cns": "3",
        "carrier": "CHINA+MOBILE",
        # "imsi": "460076002180196",
        "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; MI 5  Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36",
        "reach": "1",
        "newbie": "0",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "Keep-Alive",
        # "Cookie": "duid=59624219",
        "Host": "api.douguo.net",
        # "Content-Length": "68",
    }

    proxy = {'http': 'http://H076RR7P08B5W86P:D6B83B693E9016A2@http-pro.abuyun.com:9010'}
    # response1 = requests.get(url=url, proxies=proxy)
    #
    # print(response1.text)
    response = requests.post(url=url, headers=header, data=data)

    return response


def handle_index():
    url = 'http://api.douguo.net/recipe/flatcatalogs'
    data = {
        "client": "4",
        # "_session": "1557537321152863064010600213",
        # "v": "1557405381",
        "_vs": "2305",
    }

    response = handel_request(url=url, data=data)
    index_response_dict = json.loads(response.text)
    for index_item in index_response_dict['result']['cs']:
        # print(index_item)
        for index_item_1 in index_item['cs']:
            # print(index_item_1)
            for item in index_item_1['cs']:
                # print(item)
                data_2 = {
                    "client": "4",
                    # "_session": "1557539422131863064010600213",
                    "keyword": item['name'],
                    "order": "0",
                    "_vs": "400",
                }
                # print(data_2)
                queue_list.put(data_2)
    print(response.text)


def handle_caipu_list(data):
    print("当前处理的食材：", data['keyword'])
    caipu_list_url = 'http://api.douguo.net/recipe/v2/search/0/20'
    caipu_list_response = handel_request(url=caipu_list_url, data=data)
    # print(caipu_list_response.text)
    caipu_list_response_dict = json.loads(caipu_list_response.text)
    for item in caipu_list_response_dict['result']['list']:
        # print(item)
        caipu_info = {}
        caipu_info['shicai'] = data['keyword']
        if item['type'] == 13:
            caipu_info['user_name'] = item['r']['an']
            caipu_info['shicai_id'] = item['r']['id']
            caipu_info['describe'] = item['r']['cookstory'].replace('\n', '').replace(' ', '')
            caipu_info['caipu_name'] = item['r']['n']
            caipu_info['zuoliao_list'] = item['r']['major']
            detail_url = 'http://api.douguo.net/recipe/detail/' + str(caipu_info['shicai_id'])
            detail_data = {
                "client": "4",
                # "_session": "1557539422131863064010600213",
                "author_id": "0",
                "_vs": "2801",
                "_ext": '{"query":{"kw":'+caipu_info['shicai']+',"src":"2801","idx":"1","type":"13","id":'+str(caipu_info['shicai_id'])+'}}',
            }
            detail_response = handel_request(url=detail_url, data=detail_data)
            detail_response_dict = json.loads(detail_response.text)
            caipu_info['tips'] = detail_response_dict['result']['recipe']['tips']
            caipu_info['cook_step'] = detail_response_dict['result']['recipe']['cookstep']
            print('当前入库菜谱是：', caipu_info['caipu_name'])
            mongo_info.insert_item(caipu_info)

        else:
            continue



handle_index()

pool = ThreadPoolExecutor(max_workers=2)
while queue_list.qsize() > 0:
    pool.submit(handle_caipu_list, queue_list.get())
# handle_caipu_list(queue_list.get())
# print(queue_list.qsize())













