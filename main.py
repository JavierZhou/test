import random

foods = ['海底捞',
         '胡歌',
         '费大厨',
         '探鱼',
         '胖哥俩',
         '砂锅粥',
         '丹东',
         '微公子',
         '天台',
         '木屋']


def choose_food() -> str:
    return foods[(random.randint(0, len(foods) - 1))]


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print(choose_food())
