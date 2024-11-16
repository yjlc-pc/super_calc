from time import sleep

import 单位换算 as dwhs
import 基本 as b
import 鸡兔同笼 as cr
from 公共 import *


def n1():
    passed = 0
    while not passed:
        try:
            b.main()
        except:
            continue
        passed = 1


def n2():
    cr.main()


def n3():
    passed = 0
    while not passed:
        try:
            dwhs.main()
        except:
            continue
        passed = 1


def n4():
    output("谢谢使用")
    exit(0)


def main():
    menu("欢迎使用万能计算器！")

    print("\n")
    while 1:
        menu("菜单:\n[1]基本运算\n[2]鸡兔同笼\n[3]单位换算\n[4]退出")
        a = get_input("请选择:")
        try:
            eval("n" + a + "()")
        except NameError:
            print("请确认后输入！")
            sleep(3)
            menu("菜单:\n[1]基本运算\n[2]鸡兔同笼\n[3]单位换算\n[4]退出")
            a = get_input("请选择:")
            try:
                eval("n" + a + "()")
            except NameError:
                n4()


main()
