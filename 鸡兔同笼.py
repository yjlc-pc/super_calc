from 公共 import *
def get_data():

    return {"head":int(get_input("请输入总头数：")),
            "feet":int(get_input("请输入总脚数：")),
            "chick":int(get_input("请输入动物一（脚更少的那只）的脚数：")),
            "rabbit":int(get_input("请输入动物二（脚更多的那只）的脚数"))}

def core_calc(data: dict):
    #假设全是鸡
    鸡脚数 = data["head"] * data["chick"]
    #求多算了几只鸡
    多算 = data["feet"] - 鸡脚数
    #求兔比鸡的脚数多多少
    差 = data["rabbit"] - data["chick"]
    #要补齐几只兔
    兔 = 多算 / 差
    if not 兔 % 1 == 0:
        output("无解！")
        return
    else:
        兔 = int(兔)
    鸡 = data["head"] - 兔
    output(f"有{鸡}只动物一，有{兔}只动物二")




def main():
    core_calc(data=get_data())