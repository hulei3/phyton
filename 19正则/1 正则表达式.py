""""
1. 导入re模块
2. 使用match方法进行匹配操作
3. 使用group方法来提取数据
"""
# 1. 导入re模块
import re

# 2. 使用match方法进行匹配操作
#第一个参数正则表达式，第二个参数要匹配的字符串
match_obj= re.match("he","hello")  #保存匹配的对象
#3，使用group方法来提取数据，获取匹配结果
result = match_obj.group()
print(result)