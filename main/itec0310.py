# d=-1
# # d.key =50
# print(dir(d))
# print(d.__abs__())
# print(d.to_bytes())
# def fn():
#     return 2+2
# print(fn.__call__())
#
#
# class A:
#     id = 1
#     def say(self):
#         return f'Hi'
#     def __call__(self, *args, **kwargs):
#         return 2+2
#
# a=A()
# print(a)
# print(a())
d=1
c='1'
print(id(d))
print(id(c))
c=int(c)
print(id(c))
print(id(str(d)))
print(id(int(str(d))))
print(id(1))
print(id('1'))