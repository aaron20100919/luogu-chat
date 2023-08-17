import requests, json
from config import *
from find import *

try:
    name + ""
except:
    name = input("whom do you want to chat: ")
uid = find_user(name)


def look():
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
        "x-csrf-token": "1692341322:WPYDG2Pw9apxar80YIGxzNOUWe0S83y15Rxo9YpPleA=",
        "x-requested-with": "XMLHttpRequest",
    }

    params = {
        "user": str(uid),
    }

    response = requests.get(
        "https://www.luogu.com.cn/api/chat/record",
        params=params,
        cookies=cookies,
        headers=headers,
    )

    response.raise_for_status()

    text = json.loads(response.content)

    # from pprint import pprint
    # pprint(text)

    return text


def send(text):
    headers = {
        "authority": "www.luogu.com.cn",
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "content-type": "application/json",
        "origin": "https://www.luogu.com.cn",
        "referer": "https://www.luogu.com.cn/chat",
        "sec-ch-ua": '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203",
        "x-csrf-token": "1692342038:RKR+HboECxZzbYc9hNzY4rYR/hBxLy4vUlDdpULP3g4=",
        "x-requested-with": "XMLHttpRequest",
    }

    json_data = {
        "user": uid,
        "content": text,
    }

    response = requests.post(
        "https://www.luogu.com.cn/api/chat/new",
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    response.raise_for_status()


if __name__ == "__main__":
    while True:
        try:
            text = look()

            for message in text["messages"]["result"]:
                if message["sender"]["uid"] == uid:
                    print("%s: %s" % (name, message["content"]))
                else:
                    print(" " * 60 + "you: %s" % message["content"])

            send_text = input("\n: ") + "\n"
            while True:
                line = input()
                if line.strip():
                    send_text += line + "\n"
                else:
                    break
            if send_text.strip():
                send(send_text)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(e)
