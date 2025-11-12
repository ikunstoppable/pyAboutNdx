# from mypyfile import blockcounts, mysum

# import os

# print(mysum(1,2,3,4,5))

# print(blockcounts)


# os.remove('mypyfile.py')
# import math

# for item in range(10):
#     try:
#         input_number = input('write a number')
#         result = math.log(float(input_number))
#         print(result)
#     except Exception:
#         print('math goes wrong')
#         break

# with open('readme.txt') as myfile:
#     # content = myfile.read()
#     # print(content)

#     lines = myfile.readlines()
#     for item in range(len(lines)):
#         print(lines[item])

# with open('readme.txt') as myfile:
#     lines = myfile.readlines()
#     for item in lines:
#         print(item)
#     myfile.close()


# with open('yang_write.txt', 'w') as myfile:
#     try:
#         for i in range(100):
#             10/(50-i)
#             myfile.write(str(i) + '\n')
#     except Exception:
#         print('error:', i)
#     finally:
#         myfile.close()

# list dic set
# class people:
#     '帮助信息：minimons initing'
#     hp = 100
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print('hp = :', self.hp)

#     def display_name(self):
#         print(self.name)

# print(people.__doc__)

# p1 = people('dudu', 20)
# p2 = people('paoche', 100)

# p1.display()
# p1.display_name()
# p2.display()
# p2.display_name()

# p1.hp = 2000
# print(p1.hp)
# print(p2.hp)

# p1.name = 'chaoji'
# print(p1.name)

# del p1.age
# print(hasattr(p1, 'age'))

# print(getattr(p2, 'name'))
# setattr(p2, 'mp', 7000)
# print(getattr(p2, 'mp'))

#定义父类
# class Parent:
#     number = 100,
#     def __init__(self):
#         print('父类构造方法调用')
#     def setAttr(self, attr):
#         Parent.parentAttr = attr
#     def getAttr(self):
#         print('父类属性：' , Parent.parentAttr)
#     def overide_fn(self):
#         print('父类方法未被覆盖')
# #定义子类
# class Son(Parent):
#     def __init__(self):
#         print('子类构造函数被调用')
#     def overide_fn(self):
#         print('子类方法覆盖了父类方法')

# s1 = Son()
# print(s1.number)
# s1.overide_fn()
# s1.setAttr('yy')
# s1.getAttr()


from time import *
print(time())
print(localtime(time()))
print(asctime(localtime(time())))
print(strftime('%Y-%m-%d %H:%M:%S',localtime()))