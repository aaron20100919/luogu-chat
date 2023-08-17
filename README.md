# [用python实现洛谷聊天](https://github.com/aaron20100919/luogu-chat)

用python实现洛谷聊天

# 如果报错400那么改 `lgchat.py` 中的headers!!!

code有些多, 自己访问

使用说明, 复制`cookies`进`config.py`里, 然后运行`chatui.py`即可

还有非UI的终端版, `lgchat.py`

哦, 对了, 防止被老师看到, 只有光标移动到了上面才会显示



提前配置:

1. 下载
2. win + Q, 输入cmd
3. 输入 `pip install requests`



使用说明:

1. 先配置cookie和header
2. 打开[这个](https://www.luogu.com.cn/chat)
3. F12进入开发者模式
4. 选择网络
5. 选择fetch/xhr
6. 点击一个人
7. 右边随便一个右键复制成cURl(Bash)
8. 打开[这个](https://curlconverter.com/), 复制进去
9. 复制cookies进 `config.py`
10. 复制header进 `lgchat.py` 中的 `look()` 中的 headers
11. F12进入开发者模式
12. 选择网络
13. 选择fetch/xhr
14. 在[这个](https://www.luogu.com.cn/chat)随便选一个人发一条消息
15. 右边选new右键复制成cURl(Bash)
16. 打开[这个](https://curlconverter.com/), 复制进去
17. 复制header进 `lgchat.py` 中的 `send(text)` 中的 headers
18. 保存

快捷键说明:
1. ctrl+q 退出
2. ctrl+enter 发送
