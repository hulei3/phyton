import re
#1、*：匹配前一个字符出现0次或者无限次，即可有可无
# match_obj = re.match("tw*o","twowww.")
#  match_obj = re.match(".*","abcdefg")

#判断是否有值
# if match_obj:
 #   result = match_obj.group()
 #   print(result)
# else:
 #    print("匹配失败! ")

# 2.+：匹配前一个字符出现1次或者无限次，即至少有1次
# match_obj = re.match("tw+o","twwwwo")
# match_obj = re.match("tw*o","twwwwo")
#判断是否有值
# if match_obj:
 #  result = match_obj.group()
  # print(result)
# else:
  #  print("匹配失败! ")

# 3.?：匹配前一个字符出现1次或者0次，即要么有1次，要么没有
#match_obj = re.match("https?","https")

#判断是否有值
# if match_obj:
 #  result = match_obj.group()
 #  print(result)
# else:
 #   print("匹配失败! ")

# 4.{m}：匹配前一个字符出现m次
# match_obj = re.match("ht{2}p","http")

#判断是否有值
# if match_obj:
 #  result = match_obj.group()
 #  print(result)
#velse:
 #   print("匹配失败! ")

# 5.{m，n}：匹配前一个字符出现从m到n次
match_obj = re.match("ht{2,4}p?","https")

#判断是否有值
if match_obj:
   result = match_obj.group()
   print(result)
else:
    print("匹配失败! ")
