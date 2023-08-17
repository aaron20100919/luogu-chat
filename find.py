import requests, json
from config import *


def find_user(name):
    headers = {
        "authority": "www.luogu.com.cn",
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "referer": "https://www.luogu.com.cn/chat",
        "sec-ch-ua": '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203",
        "x-csrf-token": "1692358153:+vZpVu0IR443X2vRA0luYfE7mUG0k/ciuSbLqs3V76A=",
        "x-requested-with": "XMLHttpRequest",
    }

    params = {
        "keyword": name,
    }

    response = requests.get(
        "https://www.luogu.com.cn/api/user/search",
        params=params,
        cookies=cookies,
        headers=headers,
    )

    text = json.loads(response.content)

    return text["users"][0]["uid"]
