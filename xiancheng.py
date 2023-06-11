#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : xiancheng.py
# @Author: 理想
# @Date  : 2023/6/11 16:22
# @IDE  : PyCharm

import requests
import json
import threading
import time
import uuid

class PostRequests():
    def __init__(self):
        # 产生uuid
        u=uuid.uuid1()
        # 产生订单号
        orderID='TEST'+u.hex
        self.url='http://123.57.210.36:8091/couponWeb/couponSX/comboCouponOrderFrozen'
        self.data={"payOrderNo": orderID,"userId":"16500","activityId":"1103",
                     "couponIdNumMap":{"2580":2,"2581":2,"2582":2}
        }
        self.headers={'content-type':'application/json'}
        self.data=json.dumps(self.data)

    def post(self):
        try:
            r=requests.post(url=self.url,data=self.data,headers=self.headers)
            print(r.json())
        except Exception as e:
            print(e)

def kquan_bf():
    login=PostRequests()
    return login.post()

try:
    i=0
#     开启线程数目
    task_number=50
    print('test启动')
    time1 = time.process_time()

    while i < task_number:
        t =threading.Thread(target=kquan_bf)
        t.start()
        i += 1
        t.join()

    time2 = time.process_time()
    times = time2-time1
    for i in range(1,10):
        print(threading.current_thread().getName())

    print(times/task_number)

except Exception as e:
    print(e)

