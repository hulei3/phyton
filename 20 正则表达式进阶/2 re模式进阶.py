# import  re
#3.sub()将匹配到的数据进行替换
# resl=re.sub("\d","24","今天是3号“）
#参数4：指定要替换的次数
# resl=re.sub("\D","2","今天是4号",4)
# print(resl)

import re
#4.split()根据匹配进行切割字符串，并返回一个列表
#语法:split("切割字符","要匹配的字符串")
# xes12 = re.split(",","abc,123")
# xes12 = re.split("\d","a1b2c3")
#参数3：指定最大的分割次数
res12 = re.split("\d","a1b2c3",2)
print(res12)