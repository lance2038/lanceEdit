# 由于Python是动态语言，根据类创建的实例可以任意绑定属性。
# 给实例绑定属性的方法是通过实例变量，或者通过self变量：

class Student(object):
    def __init__(self, name):
        self.name = name


s = Student('Bob')
s.score = 90

print(s.name)


# 但是，如果类本身需要绑定一个属性可以直接在class中定义属性，这种属性是类属性，归类所有：
# 当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。
class sk(object):
    name = 'sk'


fer = sk()  # 创建实例s
print(fer.name)  # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(sk.name)  # 打印类的name属性
fer.name = 'sk.fer'  # 给实例绑定name属性
print(fer.name)  # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(sk.name)  # 但是类属性并未消失，用sk.name仍然可以访问
del fer.name  # 如果删除实例的name属性
print(fer.name)  # 再次调用fer.name，由于实例的name属性没有找到，类的name属性就显示出来了

# 从上面的例子可以看出，在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，
# 但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
# 实例属性属于各个实例所有，互不干扰；
# 类属性属于类所有，所有实例共享一个属性；
# 不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。
