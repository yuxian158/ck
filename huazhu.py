import requests
import json
from notify import send
import os
import datetime


def checkin(cookie):
    url = "https://hweb-mbf.huazhu.com/api/signIn"
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Client-Platform': 'WEB-APP',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'DNT': '1',
        'Origin': 'https://campaign.huazhu.com',
        'Referer': 'https://campaign.huazhu.com/',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36 Edg/114.0.1823.67',
        'User-Token': 'null',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'Cookie': cookie,
    }
    data = {
        'state': '1',
        'day': str(datetime.date.today().day),
    }
    r = requests.post(url, headers=headers, data=json.dumps(data)).json()
    if r['businessCode'] == "1000":
        msg = f"签到成功, 获得{r['content']['point']}积分!"
    else:
        # json内容到msg
        msg = f"签到失败\n" + json.dumps(r)
    return msg


if __name__ == "__main__":
    print(os.environ.get("hc_a"))
    send("华住会签到", checkin(os.environ.get("huazhu_cookies")))
