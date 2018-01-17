# type() 判断对象类型
# 基本类型都可以用type()判断
print('type(123) =', type(123))
print('type(\'123\') =', type('123'))
print('type(None) =', type(None))
# 如果一个变量指向函数或者类，也可以用type()判断：
print('type(abs) =', type(abs))
# 需要比较两个变量的type类型是否相同
print('type(\'abc\')==str?', type('abc') == str)
# 判断基本数据类型可以直接写int，str等，判断一个对象是否是函数可以使用types模块中定义的常量：
import types


def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# 能用type()判断的基本类型也可以用isinstance()判断 优先使用isinstance()判断类型

# 获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
dir("abc")
# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
# 在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，
# 它自动去调用该对象的__len__()方法，所以，下面的代码是等价的
print(len('ABC'), 'ABC'.__len__())
print('ABC'.lower())


class MyObject(object):

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()

print('hasattr(obj, \'x\') =', hasattr(obj, 'x'))  # 有属性'x'吗？
print('hasattr(obj, \'y\') =', hasattr(obj, 'y'))  # 有属性'y'吗？
setattr(obj, 'y', 19)  # 设置一个属性'y'
print('hasattr(obj, \'y\') =', hasattr(obj, 'y'))  # 有属性'y'吗？
print('getattr(obj, \'y\') =', getattr(obj, 'y'))  # 获取属性'y'
print('obj.y =', obj.y)  # 获取属性'y'

print('getattr(obj, \'z\') =', getattr(obj, 'z', 404))  # 获取属性'z'，如果不存在，返回默认值404

f = getattr(obj, 'power')  # 获取属性'power'
print(f)
print(f())

