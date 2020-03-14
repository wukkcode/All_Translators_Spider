import tkinter as tk
import requests as r
import json


def translateText(word):
    url = r'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    header = {
        "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36 Edg/78.0.276.20"
    }

    # some_proxies = {'http': 'http://124.205.11.245:8888'}
    form_data = {
        'i': word,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '15807895564842',
        'sign': 'f2d561d53bb76619e26218ba7e91d7b3',
        'ts': '1580789556484',
        'bv': '75a84f6fbcebd913f0a4e81b6ee54608',
        'doctype': 'json',
        'version': 2.1,
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }
    post_html = r.post(
        url,
        data=form_data,
        headers=header,
    )
    post_html.encoding = post_html.apparent_encoding
    content_dict = json.loads(post_html.text)
    target = content_dict['translateResult'][0][0]['tgt']
    return target


# ui设计
root = tk.Tk()

root.title = '有道翻译'

tk.Label(root, text='输入：').grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text='翻译：').grid(row=1, column=0, padx=10, pady=10)

oEntry1 = tk.Entry(root)
oEntry1.grid(row=0, column=1, padx=10, pady=10)
oEntry2 = tk.Entry(root)
oEntry2.grid(row=1, column=1, padx=10, pady=10)


def insertTranslateText():
    oEntry2.delete(0, 'end')
    oEntry2.insert(0, translateText(oEntry1.get()))


def deleteText():
    oEntry1.delete(0, 'end')
    oEntry2.delete(0, 'end')


tk.Button(root, text='翻译', command=insertTranslateText).grid(
    row=2,
    column=0,
    padx=10,
    pady=10,
)
tk.Button(root, text='清除', command=deleteText).grid(
    row=2,
    column=1,
    padx=10,
    pady=10,
    sticky='e',
)
root.mainloop()