# -*-coding:utf-8-*-

import urllib, httplib
from BeautifulSoup import BeautifulSoup
import re
import sys
from flask import Flask, request

URL_ZCCX = 'zccx.tyb.njupt.edu.cn'
TIME_SUM = r'<span class="badge">(\d+?)</span>'
TIME_DAY = r'(\d+?)年(\d+?)月(\d+?)日</td>'

app = Flask(__name__)

reload(sys)
sys.setdefaultencoding('utf-8')


def getcp(url, name, id):
    postp = {'name': name, 'number': id}
    params = urllib.urlencode(postp)
    headers = {"Content-type": "application/x-www-form-urlencoded"}
    conn = httplib.HTTPConnection(url)
    conn.request("POST", '/student', params, headers)
    res = conn.getresponse().read()
    conn.close()
    # soup = BeautifulSoup(res)
    time_sum_re = re.compile(TIME_SUM)
    time_sum = time_sum_re.findall(res)[0]
    # print soup
    return time_sum


# print soup.table()
# print soup.span()

# getcp(URL_ZCCX,'王家豪','B14040118')


@app.route('/zccx', methods=['GET', 'POST'])
def zccx():
    if request.method == 'POST':
        na = request.form['name']
        uid = request.form['id']
        # print name,id
        sum = getcp(URL_ZCCX, na, uid)
    return sum
    # return id


if __name__ == '__main__':
    app.run(debug=True)
