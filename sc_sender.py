import requests
from datetime import datetime
from datetime import timedelta


# 使用 Server酱 发送电量数据至微信
def send(key_url: str, data: list):
    # post请求
    requests.post(key_url, data=data)
    return


def handle(data: list, describe: str):
    # 标题
    text = ''
    #实际上最多获取到前一天的
    cur_date = (datetime.now()-timedelta(days=1)).strftime("%Y-%m-%d")
    if data[0]['date'] == cur_date:
        text = '昨日用电{:.2f}度，今日可用{:.2f}度'.format(
            data[0]['cost'], data[0]['rest'])
    else:
        text = '数据未更新(￣_￣|||)'

    # 详细内容的文本

    # 表头
    desp = describe + '\n\n'
    # 出于Sever酱的markdown表格样式问题，首行表格空格为全角空格
    desp += ('|　日期　|　当日用电　|　可用电量　|　当日充电　|\n'
             '| :---: | :------: | :------: | :------: |\n')

    # 表格数据
    for line in data:
        for datum in line:
            # float数据控制小数点为两位
            if isinstance(line[datum], float):
                desp += '| {:.2f} '.format(line[datum])
            else:
                desp += '| {} '.format(line[datum])
        desp += '|\n'

    # print(desp)  # 测试用

    data = {
        'text': text,
        'desp': desp
    }

    return data
