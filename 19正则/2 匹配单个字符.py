import re
# 1. : 匹配任意1个字符(除了\n)
# match_obj = re.match("t.o","two")
#判断是否有值
# if match_obj:
  #  result = match_obj.group()
 #    print(result)
#  else:
#    print("匹配失败! ")


# 2. : 匹配[]列举中的字符
#  match_obj = re.match("汤姆[123]","汤姆1")
# 判断是否有值
# if match_obj:
 #    result = match_obj.group()
 #   print(result)
# else:
 #   print("匹配失败! ")

# 3.\d:匹配数字, 即0-9
# match_obj=re.match("\d","3")
# #判断是否有值
# if match_obj:
 #  result = match_obj.group()
 #  print(result)
# else:
#   print("匹配失败! ")

# 4.\D：匹配非数字，即不是数字
# match_obj=re.match("\D","!")
   # 判断是否有值
# if match_obj:
 #   result = match_obj.group()
 #   print(result)
# else:
 #   print("匹配失败! ")

# 5.\s:匹配空白, 即空格, tab键
# match_obj=re.match("汤姆\s","汤姆 1")

   # 判断是否有值
# if match_obj:
  #  result = match_obj.group()
  #  print(result)
# else:
 #   print("匹配失败! ")

# 6.\S:匹配非空白
# match_obj=re.match("汤姆\S","汤姆?")

   # 判断是否有值
# if match_obj:
 #   result=match_obj.group()
 #   print(result)
# else:
 #   print("匹配失败! ")

# 7. \w:匹配非特殊字符, 即a-z, A-z, 0-9, _汉字
# match_obj=re.match("\w","_")
   # 判断是否有值
# if match_obj:
 #   result=match_obj.group()
  #  print(result)
# else:
  #  print("匹配失败! ")

# 8.\W：匹配特殊字符，即非字母，非数字，非汉字，非下划线
match_obj=re.match("\W","+")
   # 判断是否有值
if match_obj:
    result=match_obj.group()
    print(result)
else:
    print("匹配失败! ")