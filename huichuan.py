"""
new Env('汇川论坛');
"""

import requests
import json
from notify import send
import os


def checkin(authorization):
    url = "https://zshc.inovance.com/apipc/community/v1/sign/add"
    headers = {
        "content-type": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Xauthorization": authorization,
    }
    data = {"taskId": "21"}
    r = requests.post(url, headers=headers, data=json.dumps(data)).json()
    res_text = ""
    if r.get("code") == 200:
        res_text = "签到成功"
    else:
        res_text = r.get("message")
    return res_text


if __name__ == "__main__":
    print(os.environ.get("hc_a"))
    send("汇川论坛", checkin(os.environ.get("hc_a")))
