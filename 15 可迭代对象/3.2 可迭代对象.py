# 可迭代对象:Iterable 和 迭代器对象: Iterator
from collections. abc import Iterable, Iterator
name = "maiva"
print(isinstance(name, Iterable))  # True:
print(isinstance(name, Iterator))  # False
it = iter(name)
print(isinstance(it, Iterable))
print(isinstance(it, Iterator))

#总结：可迭代对象不一定是迭代器对象，但是迭代器对象一定是可迭代对象