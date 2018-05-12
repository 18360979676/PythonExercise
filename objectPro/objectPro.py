__author__ = 'lyl'

# 给类实例动态绑定属性和方法


class Student(object):
    # __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


if __name__ == '__main__':
    s = Student()
    s.name = 'lyl'
    # print(s.name)

    # def set_age(self, age):
    #     self.age = age
    # from types import MethodType
    # s.set_age = MethodType(set_age, s)  # 给实例对象单独绑定方法
    # s.set_age(25)
    # print(s.age)

    # 给所有类的实例对象绑定方法
    def set_score(self, score):
        self.score = score
    Student.set_score = set_score

    s2 = Student()
    s2.set_score(99)
    print(s2.score)
