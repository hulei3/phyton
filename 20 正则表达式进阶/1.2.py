import re
# 2. findall()以列表形式返回匹配到的字符串
# findall_obj = re. findall("ab", "abaabaaabaaaab")
# findall_obj=re.findall("\d","a1b2c3")
# finda11_obj=re.findall("[a-z]","a1b2c3")
# finda11_obj=re.findall("[^\d]","a1b2c3")
# findall_obj=re.findall("[^[a-z]]","a1b2c3")
#如果没有匹配到的子串，返回空列表
findall_obj=re.findall("\d","a.b.c")
# 注意点: 1. 不需要调用group函数, 2. finda11匹配所有的符合项
print(findall_obj)