# defination a function for get square by number
def f(x):
    return x * x


# 1. for circulation
l = []
for n in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    l.append(f(n))
print(l)
# 2. list
k = [x * x for x in range(10)]
print(k)
# 3. generator
s = []
g = (x * x for x in range(10))
for i in g:
    s.append(i)
print(s)
# 4.create a new map
# map。map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
r = map(f, list(range(0, 10)))
print(list(r))
# eg.map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串
print(list(map(str, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])))
