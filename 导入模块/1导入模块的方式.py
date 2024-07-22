# 需求:math模块下sqrt()开平方计算
'''
1 导入模块
2 调用模块的函数功能
'''
# 1 方法1 import 模块名，模块名，功能名（）
import math
print(math.sqrt(9))

# 2 方法2: 语法: from 模块名 import 功能1，功能2，功能3（不需要书写模块名，功能）
from math import sqrt
print(sqrt(9))

# 3  方法3  from 模块名 import*
from math import*
print(sqrt(9))

# 需求:运行后暂停2秒打印hello
"""
1 导入time模块或导入sleep功能
2调用功能
3 打印hello
"""
import time as tt
tt.sleep
print("hello")