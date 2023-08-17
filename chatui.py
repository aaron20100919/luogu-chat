import tkinter as tk
from tkinter import scrolledtext
from lgchat import *

wait_time = 5 * 1000  # 自定义更改
leave_alpha = 0.3  # 自定义更改

root = tk.Tk()
root.geometry("200x400+800+400")
root.attributes("-topmost", True)

get_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, height="25")
get_box.pack(padx=30)

send_box = tk.Text(height="3", width="20")
send_box.pack(padx=30)


def get_history():
    text = look()
    get_box.config(state=tk.NORMAL)
    get_box.delete("1.0", "end")
    for message in text["messages"]["result"]:
        if message["sender"]["uid"] == uid:
            get_box.insert("end", "%s: %s\n\n" % (name, message["content"]))
        else:
            get_box.insert("end", "you: %s\n" % message["content"])

    get_box.config(state=tk.DISABLED)
    get_box.see(tk.END)


def repeat_get_history():
    get_history()
    root.after(wait_time, repeat_get_history)


def send_text(event=None):
    text = send_box.get("1.0", "end")
    send_box.delete("1.0", "end")
    send(text)
    get_history()


def exit(event=None):
    root.destroy()


def enter(event=None):
    root.attributes("-alpha", 1)


def leave(event=None):
    root.attributes("-alpha", leave_alpha)


root.bind("<Control-Return>", send_text)
root.bind("<Control-q>", exit)
root.bind("<Enter>", enter)
root.bind("<Leave>", leave)

send_button = tk.Button(command=send_text, text="send")
send_button.pack(side=tk.RIGHT)

if __name__ == "__main__":
    get_history()
    root.after(wait_time, repeat_get_history)
    root.mainloop()
