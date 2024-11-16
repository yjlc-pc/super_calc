重量 = {"mg": 0, "g": 1000, "kg": 1000000, "t": 1000000000}
时间 = {"ms": 0, "s": 1000, "min": 60000, "h": 3600000, "day": 86400000}
长度 = {"mm": 0, "cm": 10, "dm": 100, "m": 1000, "km": 1000000}
面积 = {"mm_": 0, "cm_": 100, "dm_": 10000, "m_": 1000000, "公顷": 10000000000, "km_": 1000000000000}
人民币 = {"分": 0, "角": 10, "元": 100}
中文名 = {"毫克": 0, "克": 1000, "千克": 1000000, "吨": 1000000000,
          "毫秒": 0, "秒": 1000, "分钟": 60000, "小时": 3600000, "天": 86400000,
          "毫米": 0, "厘米": 10, "分米": 100, "米": 1000, "千米": 1000000,
          "平方毫米": 0, "平方厘米": 100, "平方分米": 10000, "平方米": 1000000, "平方千米": 1000000000000}

from 公共 import *


def get_data():
    a = get_input("请输入你要换算的数(数字和单位间用空格隔开，如：\"35 kg\",如要输入²,请替换为:_):")
    a = a.split()
    if len(a) != 2:
        raise ValueError
    else:
        a[0] = int(a[0])
        b = get_input("请输入换算后的单位：(如要输入²,请替换为\"_\")")
        return {"要换算的数": a[0], "yhsddw": a[1], "换算后的单位": b}


def core_calc(data: dict):
    first = 0
    then = 0
    first, then = method_name(data, first, then)

    if first == 0 or then == 0:
        output("暂不支持转换此类型！")
    else:
        if then > first:
            进率 = then // first
            output(str(data["要换算的数"] / 进率) + data["换算后的单位"])
        elif then < first:
            进率 = first // then
            output(str(data["要换算的数"] * 进率) + data["换算后的单位"])


def method_name(data, first, then):
    temp = 0

    for i in 重量.keys():
        if i == data["yhsddw"]:
            first = 重量[i]
            temp = 1
        elif i == data["换算后的单位"]:
            then = 重量[i]
    if temp == 1:
        return first, then

    for i in 时间.keys():
        if i == data["yhsddw"]:
            first = 时间[i]
            temp = 1

        elif i == data["换算后的单位"]:
            then = 时间[i]

    if temp == 1:
        return first, then

    for i in 长度.keys():
        if i == data["yhsddw"]:
            first = 长度[i]
            temp = 1
        elif i == data["换算后的单位"]:
            then = 长度[i]

    if temp == 1:
        return first, then

    for i in 面积.keys():
        if i == data["yhsddw"]:
            first = 面积[i]
            temp = 1
        elif i == data["换算后的单位"]:
            then = 面积[i]

    if temp == 1:
        return first, then

    for i in 人民币.keys():
        if i == data["yhsddw"]:
            first = 人民币[i]
            temp = 1
        elif i == data["换算后的单位"]:
            then = 人民币[i]

    if temp == 1:
        return first, then

    for i in 中文名.keys():
        if i == data["yhsddw"]:
            first = 中文名[i]
            temp = 1
        elif i == data["换算后的单位"]:
            then = 中文名[i]

    if temp == 1:
        return first, then


def main():
    core_calc(data=get_data())
