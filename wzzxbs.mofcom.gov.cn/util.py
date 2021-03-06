import requests
import time
import openpyxl
import random
import datetime

def get_headers():
    pc_headers = {
        "X-Forwarded-For": '%s.%s.%s.%s' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
    }
    return pc_headers


class NetWorkError(Exception):
    pass


def build_request(url, headers=None,data=None):
    if headers is None:
        headers = get_headers()
    for i in range(3):
        try:
            if data:
                response=requests.post(url,data=data,headers=headers,timeout=15)
            else:
                response = requests.get(url, headers=headers, timeout=15)
            return response
        except:
            continue
    raise NetWorkError

def write_to_excel(lines,filename,write_only=True):
    excel=openpyxl.Workbook(write_only=write_only)
    sheet=excel.create_sheet()
    for line in lines:
        sheet.append(line)
    excel.save(filename)

def get_next_date(current_date='2017-01-01'):
    current_date=datetime.datetime.strptime(current_date,'%Y-%m-%d')
    oneday = datetime.timedelta(days=1)
    next_date = current_date+oneday
    return str(next_date).split(' ')[0]

def current_time():
    return time.strftime("%Y-%m-%d %H:%M:%S")

def load_txt(filename):
    for line in open(filename,'r'):
        try:
            item=json.loads(line)
        except:
            continue
        yield item

        

