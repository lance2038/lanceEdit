# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
# 调用函数f()时，才真正计算求和的结果
f = lazy_sum(1, 2, 4, 5, 7, 8, 9)
print(f)
print(f())
# 我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”

# 注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：

k1 = lazy_sum(1, 3, 5, 7, 9)
k2 = lazy_sum(1, 3, 5, 7, 9)
print(k1 == k2)


# why f1(), f2(), f3() returns 9, 9, 9 rather than 1, 4, 9?
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())


# fix:
def count():
    fs = []

    def fk(n):
        def j():
            return n * n

        return j

    for i in range(1, 4):
        fs.append(fk(i))
    return fs


f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())

# 返回函数
