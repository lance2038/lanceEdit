from functools import reduce


def fn(x, y):
    # print('x:' + str(x))
    # print('y:' + str(y))
    # print('R:' + str(x * 10 + y))
    return x * 10 + y


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(fn, [1, 3, 5, 7, 9]))

print(reduce(fn, map(char2num, '13579')))
# reduce()函数接收的参数和 map()类似，一个函数 f，一个list，但行为和 map()不同，reduce()传入的函数 f 必须接收两个参数，
# reduce()对list的每个元素反复调用函数f，并返回最终结果值。
