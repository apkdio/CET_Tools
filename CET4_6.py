import csv
import json
import time
from urllib.parse import quote, unquote

import pandas as pd
import requests

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.95 Safari/537.36",
    "Origin": "https://cjcx.neea.edu.cn",
    "Referer": "https://cjcx.neea.edu.cn/html1/folder/21083/9970-1.htm",
    "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site"
}
cookie = {"DNT": 1}
name = quote(input("输入姓名:"))
identity_id = input("请输入身份证号:")
count = 0
cet = ""
score = 0
c_pass = None
try:
    for km in range(1, 3):
        url = f"https://cachecloud.neea.cn/latest/results/cet?km={km}&xm={name}&no={identity_id}&source=pc"
        response = requests.get(url, headers=header)
        res_data = json.loads(response.text)
        if res_data["code"] == 404:
            if count == 1:
                count = 0
            count += 1
        else:
            if km == 1:
                cet = "CET4"
            else:
                cet = "CET6"
            score = res_data["score"]
            if int(score) >= 425:
                c_pass = "PASS"
            else:
                c_pass = "FAIL"
    print(name, identity_id, cet, score, c_pass)
except Exception as e:
    print("获取失败! 原因:",e)