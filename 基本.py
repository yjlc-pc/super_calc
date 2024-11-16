from 公共 import *
def get_data():
    menu("菜单：\n[1]加法\n[2]减法\n[3]乘法\n[4]除法\n[5]除法(四舍五入求整)\n[6]平方\n[7]阶乘")
    a = int(get_input("请选择："))
    if a == 1:
        b = int(get_input("请输入第一个数："))
        d = "+"
        c = int(get_input("请输入第二个数："))
    elif a == 2:
        b = int(get_input("请输入第一个数："))
        d = "-"
        c = int(get_input("请输入第二个数："))
    elif a == 3:
        b = int(get_input("请输入第一个数："))
        d = "*"
        c = int(get_input("请输入第二个数："))
    elif a == 4:
        b = int(get_input("请输入被除数："))
        d = "/"
        c = int(get_input("请输入除数："))
    elif a == 5:
        b = int(get_input("请输入被除数："))
        d = "//"
        c = int(get_input("请输入除数："))
    elif a == 6:
        b = int(get_input("请输入第一个数："))
        d = "**"
        c = int(get_input("请输入次方："))

    elif a == 7:
        b = int(get_input("请输入一个数："))
        return str(b) + "-"
    else:
        raise ValueError
    return str(b) + d + str(c)

def core_calc(data):
    if data[-1] == "-":
        def 阶乘(n):
            if n == 1:
                return 1
            else:
                return 阶乘(n-1)*n
        output(阶乘(int(data[0:-1])))
    else:
        output(eval(data))

def main():
    core_calc(data=get_data())