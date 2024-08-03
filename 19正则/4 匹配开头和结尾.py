import re
# 1.^：匹配字符串开头
# match_obj = re.match("\d","1abc")
#判断是否有值
# if match_obj:
#   result = match_obj.group()
 #  print(result)
# else:
#    print("匹配失败! ")

# 2.$：匹配字符串结尾
# match_obj = re.match(".*\d$","abc3")

#判断是否有值
# if match_obj:
 #   result = match_obj.group()
 #  print(result)
# else:
#    print("匹配失败! ")
# 前后固定，中间不管
# match_obj = re.match("\d.*\d$","2abcd3")

#判断是否有值
#if match_obj:
 #  result = match_obj.group()
#   print(result)
# else:
#    print("匹配失败! ")

# 3.[^指定字符]：除了指定字符以外都匹配
match_obj = re. match("^\d.*[^36]", "2abcd6")
#判断是否有值
if match_obj:
   result = match_obj.group()
   print(result)
else:
    print("匹配失败! ")

# “匹配分组相关正则表达式”
