# coding=utf-8
import hashlib
import base64
import six
import hashlib
from urllib.parse import quote, unquote
import time
import datetime
import calendar
from datetime import timedelta


class Python_Small_Module():
    def __init__(self):
        pass

    def _safe_data(self, data):
        '''
        python2   str  === python3   bytes
        python2   uniocde === python3  str
        :param data: 给定的原始数据
        :return: 二进制类型的字符串数据
        '''
        if six.PY3:
            if isinstance(data, bytes):
                return data
            elif isinstance(data, str):
                return data.encode()
            else:
                raise Exception("请提供一个字符串")  # 建议使用英文来描述
        else:
            if isinstance(data, str):
                return data
            elif isinstance(data, unicode):
                return data.encode()
            else:
                raise Exception("请提供一个字符串")  # 建议使用英文来描述

    def encryption_urlencode(self, params_str):
        '''
        url编码
        :return:
        '''
        return quote(params_str, 'utf-8')

    def encryption_b64(self, params_str):
        '''
        base64加密
        :return:
        '''
        return str(base64.b64encode(params_str.encode('utf-8')), 'utf-8')

    def encryption_md5(self, params_str):
        '''
        base64加密
        :return:
        '''
        hs = hashlib.md5()
        hs.update(params_str.encode("utf8"))
        return hs.hexdigest()

    def decryption_urldecode(self, params_str):
        '''
        url解码
        :return:
        '''
        return unquote(params_str, 'utf-8')

    def decryption_b64(self, params_str):
        '''
        base64解密模块
        :return:
        '''
        return str(base64.b64decode(params_str.encode('utf-8')), 'utf-8')


    # ---------------------------------------------------------------------------------------------------------

    def decoding_ncr_str(self, params_str):
        '''
        NCR字符串解码
        :return:
        '''
        return params_str.replace(';', '').replace('&#x', '\\u').encode('utf-8').decode('unicode_escape')

    def decoding_unicode_str(self, params_str):
        '''
        unicode字符串解码
        :return:
        '''
        return params_str.encode('utf-8').decode('unicode_escape')

    # ---------------------------------------------------------------------------------------------------------

    def date_ago_date(self, date, days=1):
        '''
        获取指定日期前i天的日期
        默认为前一天日期，如需指定天数，请传入参数days=天数
        :param date: 日期 (str)
        :param i: 前几天 (int)
        :return: 指定日期前i天的日期  (str)
        '''
        t = time.strptime(date, "%Y-%m-%d")
        y, m, d = t[0:3]
        Date = str(datetime.datetime(y, m, d) - datetime.timedelta(days)).split()
        return Date[0]

    def day_before_date(self, date, days, the_day):
        if int(the_day) == 1:
            days_list = [self.date_ago_date(date, days=i) for i in range(int(the_day), int(days) + 1)]
        else:
            days_list = [self.date_ago_date(date, days=i) for i in range(int(the_day), int(days))]
        return days_list[::-1]

    def date_ago_days(self, date=None, days=30, the_day=1):
        '''
        获取指定日期前n天所有日期列表
        默认指定日期为当天
        默认返回前30天日期，如需返回指定天数前的日期，请传入参数 days=指定天数
        默认不包含当天日期，如需包含当天日期的话，请传入参数 the_day=0
        :param date: 指定日期 （str）
        :return: 前n天日期列表  （list）
        '''
        if not date:
            # 获取今天日期
            date = time.strftime("%Y:%m:%d").replace(':', '-') # str 例：2019-11-12
        return self.day_before_date(date, days, the_day)

    def date_month_has_days(self, date):
        '''
        获取指定月份总共有多少天
        :param date: 2019-11
        :return: int类型 #(5,30) # 输出的是一个元组，第一个元素是月份（0-11），第二个元素是这个月的天数。
        '''
        monthRange = calendar.monthrange(int(date.replace('-', '')[0:4]), int(date.replace('-', '')[4:6]))
        return monthRange[1]

    def date_week_first_last(self, date=None):
        '''
        获取指定日期上一周的开始日期和结束日期
        默认获取上周
        :param date: 2019-11
        :return: list类型  ['2019-11-04 00:00:00', '2019-11-10 23:59:59']
        '''
        d = datetime.datetime.now()
        if date:
            d = datetime.datetime.strptime(date, "%Y-%m-%d")
        dayscount = datetime.timedelta(days=d.isoweekday())
        dayto = d - dayscount
        sixdays = datetime.timedelta(days=6)
        dayfrom = dayto - sixdays
        date_from = datetime.datetime(dayfrom.year, dayfrom.month, dayfrom.day, 0, 0, 0)
        date_to = datetime.datetime(dayto.year, dayto.month, dayto.day, 23, 59, 59)
        # print('---'.join([str(date_from), str(date_to)]))
        return [str(date_from), str(date_to)]

    def date_month_first_last(self, date=None):
        """
        获取指定日期上一月的开始日期和结束日期
        默认获取上月
        :param date: 2019-11
        :return: list类型  ['2019-10-01 00:00:00', '2019-10-31 23:59:59']
        """
        d = datetime.datetime.now()
        if date:
            d = datetime.datetime.strptime(date, "%Y-%m-%d")
        dayscount = datetime.timedelta(days=d.day)
        dayto = d - dayscount
        date_from = datetime.datetime(dayto.year, dayto.month, 1, 0, 0, 0)
        date_to = datetime.datetime(dayto.year, dayto.month, dayto.day, 23, 59, 59)
        return [str(date_from), str(date_to)]

    def gen_dates(self, b_date, days):
        day = timedelta(days=1)
        for i in range(days):
            yield b_date + day * i

    def date_between_days(self, start_date, end_date=None):
        """
        获取两个日期之间的所有日期,包含开始日期和结束日期
        默认结束日期为当天
        :param start: 开始日期
        :param end: 结束日期
        :return: list类型
        """
        if not end_date:
            today = datetime.date.today()
            end_date = today.strftime('%Y-%m-%d')
        if start_date is not None:
            start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        if end_date is None:
            end = datetime.datetime.now()
        else:
            end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        between_days = [d.strftime("%Y-%m-%d") for d in self.gen_dates(start, ((end - start).days + 1))]    # d:datetime.datetime  类型
        return between_days

    # ---------------------------------------------------------------------------------------------------------

    def change_datetime_str(self, date=None):
        '''
        datetime类型的日期转换成str类型的日期
        默认为当天日期
        :param date:
        :return:
        '''
        if not date:
            date = datetime.datetime.now()
        return date.strftime('%Y-%m-%d %H:%M:%S')

    def change_datetime_timestamp(self, date=None):
        '''
        datetime类型的日期转换成int类型的时间戳 （时间戳精确到秒，即10位数的）
        默认为当天日期
        :param date:
        :return:
        '''
        if not date:
            date = datetime.datetime.now()
        date = date.strftime('%Y-%m-%d %H:%M:%S')
        return int(time.mktime(time.strptime(date, '%Y-%m-%d %H:%M:%S')))  # 1482286976.0

    def change_str_datetime(self, date=None):
        '''
        str类型的日期转换成datetime类型的日期
        默认为当天日期
        :param date:
        :return:
        '''
        if not date:
            today = datetime.datetime.now()
            date = today.strftime('%Y-%m-%d %H:%M:%S')
        return datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")

    def change_str_timestamp(self, date=None):
        '''
        str类型的日期转换成int类型的时间戳 （时间戳精确到秒，即10位数的）
        默认为当天日期
        :param date:
        :return:
        '''
        if not date:
            today = datetime.datetime.now()
            date = today.strftime('%Y-%m-%d %H:%M:%S')
        return int(time.mktime(time.strptime(date, '%Y-%m-%d %H:%M:%S')))  # 1482286976.0

    def change_timestamp_datetime(self, timestamp=None):
        '''
        float类型或int类型的时间戳转化成datetime类型的日期
        默认为当前时间戳
        :param date:
        :return:
        '''
        if not timestamp:
            timestamp = time.time()
        # 先转成字符串
        st = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
        # 字符串 转成 datetime类型
        return datetime.datetime.strptime(st, "%Y-%m-%d %H:%M:%S")

    def change_timestamp_str(self, timestamp=None):
        '''
        float类型或int类型的时间戳转化成str类型的日期
        默认为当前时间戳
        :param date:
        :return:
        '''
        if not timestamp:
            timestamp = time.time()
        return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(timestamp))






if __name__ == '__main__':

    p = Python_Small_Module()

    print(p.encryption_urlencode('http://fanyi.youdao.com/'))
    print(p.encryption_b64('admin'))
    print(p.encryption_md5('http://fanyi.youdao.com/'))
    print(p.decryption_urldecode('http%3A%2F%2Ffanyi.youdao.com%2F'))
    print(p.decryption_b64('YWRtaW4='))
    print(p.decoding_ncr_str('&#x3010;&#x8BD5;&#x547C;&#x3011;'))
    print(p.decoding_unicode_str('li\u003eTurn'))
    b = u'\u4eba\u751f\u82e6\u77ed\uff0cpy\u662f\u5cb8'  # 直接打印出来 ————》 人生苦短，py是岸
    print(b)
    b = r'\u4eba\u751f\u82e6\u77ed\uff0cpy\u662f\u5cb8'
    print(p.decoding_unicode_str(b))

    # print(p.date_ago_days(days=10, the_day=0))
    # print(p.date_ago_date('2019-11-12', days=0))
    # print((p.date_month_has_days('2019-11')))
    # print(p.date_week_first_last())
    # print(p.date_month_first_last())
    # print(p.date_between_days('2019-11-01', '2019-11-06'))
    # print((p.change_datetime_str()))
    # print((p.change_datetime_timestamp()))
    # print(p.change_str_datetime('2019-11-01 00:00:00'))
    # print(p.change_str_timestamp('2019-11-01 10:20:20'))
    # print(p.change_timestamp_datetime(1573546992))
    # print(p.change_timestamp_str())