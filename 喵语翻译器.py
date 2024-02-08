# coding=UTF-8

# Author: Loveaabb
# Licence of the code: CC0
MEOW = '喵'
CHAR_SPLIT = '咪'
NUM_SPLIT = '|'

VERSION = 'v0.1 alpha'
WELCOME = '欢迎使用喵语翻译器 %s！(=^·ω·^=)\n输入 help 查看帮助喵\n' % (VERSION)

HELP = {'help': ['使用这个命令查看帮助喵', '用法：\nhelp: 显示帮助文本\nhelp 命令: 显示命令详细用法'],
        'hm': ['将人类语转换为喵语', '用法: \nhm 人类语言文本'],
        'mh': ['将喵语转换为人类语', '用法: \nmh 喵语文本'],
        'exit': ['退出本喵的翻译程序', '用法: \n本喵掐爪一算，你已经会用这个命令了喵']}


def remove_invalid_chars(s: str) -> str:
    res = ""
    for char in s:
        if char in (MEOW, CHAR_SPLIT, NUM_SPLIT):
            res += char

    return res


def meow2human(inputstr: str) -> str:
    instr = remove_invalid_chars(inputstr)
    instr = instr.split(NUM_SPLIT + CHAR_SPLIT + NUM_SPLIT)
    instr = [a.split(NUM_SPLIT) for a in instr]
    reslst = []
    res = ""

    for char in instr:
        reslst.append(0)
        for num in char:
            reslst[-1] = reslst[-1] * 8 + num.count(MEOW) - 1

    #print(reslst) #TEST

    for num in reslst:
        res += chr(num)

    return res


def human2meow(inputstr: str) -> str:
    res = ""

    for char in inputstr:
        curord_o = oct(ord(char))
        curc = curord_o.lstrip('0o')
        for n in curc:
            res += MEOW * (int(n) + 1)
            res += ' ' + NUM_SPLIT + ' '
        res += CHAR_SPLIT + ' ' + NUM_SPLIT + ' '

    res = res.rstrip(' ' + NUM_SPLIT + ' ' + CHAR_SPLIT + ' ' + NUM_SPLIT + ' ')

    return res


def hasparam(params):
    return len(params) > 0


def main():
    print(WELCOME)
    while True:
        instr = input('喵语翻译器 > ')
        cmdlst = instr.strip(' ').split()
        params = [a for a in cmdlst[1:]]

        if len(cmdlst) > 0:
            cmd = cmdlst[0]
            if cmd == 'help':
                if hasparam(params):
                    try:
                        cmd_that_a_stupid_human_cannot_use = HELP[params[0]]
                    except KeyError:
                        print('Error: help: %s: 这是个啥喵？？？\n' % (params[0]))
                        continue
                    print(params[0]+':\n')
                    print(cmd_that_a_stupid_human_cannot_use[1])
                else:
                    print('输入 "help 命令" 查看命令详细用法喵\n')
                    for k, v in HELP.items():
                        print('%s: %s' % (k, v[0]))
            elif cmd == 'hm':
                if not hasparam(params):
                    print('Error: hm: 需要参数才能转换喵！')
                    print('用法：hm 人类语言文本\n')
                    continue
                realparam = ' '.join(params)
                print('转换结果：\n---------------------------------------------\n')
                print(human2meow(realparam))

            elif cmd == 'mh':
                if not hasparam(params):
                    print('Error: mh: 需要参数才能转换喵！')
                    print('用法：mh 喵语文本\n')
                    continue
                realparam = ''.join(params)
                print('转换结果：\n---------------------------------------------\n')
                print(meow2human(realparam))

            elif cmd == 'exit':
                print('下次再见喵！')
                exit(0)

            else:
                print('Error: %s: 这是什么东西喵？' % (cmd))

            print('')



if __name__ == '__main__':
    main()
