import re
#1.search()：会扫描整个字符串并返回第一个成功的匹配
#保存返回匹配对象
# search_obj = re.search("4","今天是4号")
search_obj=re.search("\d+","今天是24号")
# 调用group函数，获取匹配结果
print(search_obj.group())