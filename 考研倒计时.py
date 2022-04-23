import requests
import json
import datetime
import time

global contents
contents = ''


def sign():
    # 金山词霸每日一句
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    r = json.loads(r.text)
    content = r["content"]
    note = r["note"]
    daily_sentence = content + "\n" + note

    # 获取日期和倒计时
    a = datetime.datetime.now()  # 实施时间
    y = str(a.year)
    m = str(a.month)
    d = str(a.day)  # 转换为字符串，便于打印
    time = y + '年' + m + '月' + d + '日' + '\n'
    b = datetime.datetime(2021, 12, 25)  # 自己设置的研究生考试时间
    count_down = (b - a).days  # 考研倒计时
    count_down = '考研倒计时{}天，加油哦！'.format(count_down)

    # qq推送
    qqtalk = 'https://qmsg.zendee.cn/send/b2d0c46d980da887d80155577f59bc1f?msg=' + count_down + '\n' + daily_sentence + '&qq=249934051,1529069592'
    requests.get(qqtalk)