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
        # 你的headers
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
        # 你的headers
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
