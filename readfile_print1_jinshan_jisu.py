# /usr/bin/python3
# _*_ coding : utf-8 _*_
# Jisunet http://www.jsxiaoshi.com/competition_rank.html
import random as rand
import time
from pynput import keyboard as kb
from pynput.keyboard import Controller as key_col
from pynput.keyboard import Key as ky
from pynput.mouse import Button, Controller

lis = ['#签到', '#打卡']
lis1 = ['生姜烧', '鳜鱼', '蒜蓉汤', '鲑鱼', '杏鲍菇', '鲍鱼', '醋饭', '鲷鱼烧', '拉面', '海鲜汤', '牛尾汤', '橙醋蟹', '海胆汤', '炒牡蛎', '大阪烧', '春卷', '泡菜烧', '鸡肉串', '铜锣烧', '荞麦面', '鳗鱼饭', '苹果饼', '奶酪饼', '阿富汗披萨', '玉子烧', '糖醋排骨', '明太鱼', '鳕鱼烧', '五花肉', '章鱼烧', '西京烧', '麻婆豆腐', '担担面', '里脊',
        '牛霖肉', '三文鱼', '酒蒸蛤蜊', '关东煮', '寿喜锅', '三明治', '蛋包饭', '牛肉饭', '寿喜烧', '甜点',
        '牛舌', '泡菜鱼', '牛肉煮', '盐渍鲭鱼意面', '虾仁']
lis2 = [',', '啊', '不错']
# 签到


class MyException(KeyboardInterrupt):
    def __init__(self, key):
        super(self).__init__()
        self.key = key

    # 'Program interrupted by user.'
    def with_traceback(self,):
        self.with_traceback()


def keyboard_input(string):
    # control the keyboard
    keyboard = key_col()
    # keyboard input text
    keyboard.type(string)
    # # Press and release space
    # keyboard.press(ky.enter)
    # keyboard.release(ky.enter)


def mouse_click():
    # control mouse
    mouse = Controller()
    mouse.press(Button.left)
    mouse.release(Button.left)
    print(mouse.position)


def on_press(key):
    if key == kb.Key.esc:
        raise MyException(key)


def main(number, string):
    # with kb.Listener(
    #     on_press=on_press) as listener:
    #     try:
    #         listener.join()
    #     except MyException as e:
    #         print('{0} was pressed'.format(e.args[0]))
    # 签到
    print('----start----')
    time.sleep(5)
    try:
        for i in range(number):
            # count of record input
            # time.sleep(60 * 20  + 5 + i)
            if ((i & 1) == 0):
                mouse_click()
                keyboard_input(lis1[rand.randint(0, number-1)] + ',')
                # mouse_click()
                time.sleep(12 + i)
                keyboard_input(lis[0])
                # mouse_click()
                print('{0} is finished -- {1} left'.format(i, number - i))
                time.sleep(60 * 20 + 5 + i)
            else:
                keyboard_input(lis1[rand.randint(0, number-1)] + ',')
                # mouse_click()
                time.sleep(12 + i)
                keyboard_input(lis[1])
                # mouse_click()
                print('{0} is finished -- {1} left'.format(i, number - i))
                time.sleep(60 * 20 + 3 + i)
    except Exception as e:
        print('{0} was pressed'.format(e.args[0]))


def main_read_file():
    # with kb.Listener(
    #     on_press=on_press) as listener:
    #     try:
    #         listener.join()
    #     except MyException as e:
    #         print('{0} was pressed'.format(e.args[0]))
    # 签到
    print('----start----')
    time.sleep(5)
    try:
        mouse_click()
        with open("D:\\python_project\\demopress\\readfile_jisu.txt", "r", encoding="utf-8") as fp:
            for line in fp.readlines():
                # print(line)
                time.sleep(3)
                # myline = line.encode("gbk")
                for it in line:
                    keyboard_input(it)
                    time.sleep(0.2)
                    time.sleep(rand.randint(1, 2) * 0.1)
    #         if ((i & 1) == 0):
    #             mouse_click()
    #             keyboard_input(lis1[rand.randint(0, number-1)] + ',')
    #             # mouse_click()
    #             time.sleep(12 + i)
    #             keyboard_input(lis[0])
    #             # mouse_click()
    #             print('{0} is finished -- {1} left'.format(i, number - i))
    #             time.sleep(60 * 20 + 5 + i)
    #         else:
    #             keyboard_input(lis1[rand.randit(0, nnumber-1)] + ',')
    #             # mouse_click()
    #             time.sleep(12 + i)
    #             keyboard_input(lis[1])
    #             # mouse_click()
    #             print('{0} is finished -- {1} left'.format(i, number - i))
    #             time.sleep(60 * 20 + 3 + i)
    except Exception as e:
        print('{0} was pressed'.format(e.args[0]))


def main1(number, string):
    lis = ['#签到', '#打卡']
    lis1 = ['糖醋排骨', '明太鱼', '鳕鱼烧', '五花肉', '章鱼烧', '西京烧', '麻婆豆腐', '担担面', '里脊',
            '牛霖肉', '三文鱼', '酒蒸蛤蜊', '关东煮', '寿喜锅', '三明治', '蛋包饭', '牛肉饭', '寿喜烧', '甜点',
            '牛舌', '泡菜鱼', '牛肉煮', '盐渍鲭鱼意面',]
    # lis2 = [',', '啊','不错']
    # with kb.Listener(
    #     on_press=on_press) as listener:
    #     try:
    #         listener.join()
    #     except MyException as e:
    #         print('{0} was pressed'.format(e.args[0]))

    print('----start----')
    time.sleep(5)
    for i in range(number):
        # count of record input
        # time.sleep(60 * 20  + 5 + i)
        if ((i & 1) == 0):
            keyboard_input(lis1[rand.randint(0, number-1)] + ',')
            mouse_click()
            time.sleep(12 + i)
            keyboard_input(lis[0])
            mouse_click()
            time.sleep(60 * 20 + 5 + i)
        else:
            keyboard_input(lis1[rand.randint(0, number-1)] + ',,')
            mouse_click()
            time.sleep(16 + i)
            keyboard_input(lis[1])
            mouse_click()
            time.sleep(60 * 20 + 3 + i)
    print('----stop----')


if __name__ == '__main__':
    # main(len(lis1), '----test----')
    main_read_file()
