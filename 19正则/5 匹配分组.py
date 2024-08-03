import re
# 1.|：匹配左右任意一个表达式
#颜色列表
# color_list=["bule","yellow","red","black","pink"]
# for value in color_list:
 #    match_obj=re.match("bule|yellow",value)
 #    if match_obj:
  #       result = match_obj.group()
   #      print(f"我喜欢的颜色是: {result}")
   #  else:
 #       print(f"我不喜欢的颜色是: {value}")
#2.(ab)：将括号中字符作为一个分组
# 需求: 匹配出163,126, qq邮箱,格式: 邮箱名@  126.com
# match_obj=re.match("[a-zA-Z0-9_]{4,20}@(163|126|qq).com","hello@qq.com")
# match_obj=re.match("[a-zA-Z0-9_]{4,20}@(163|126|qq).com","hello@qq.com")

#判断是否有值
# if match_obj:
#    result = match_obj.group()
 #   print(result)
# else:
 #   print("匹配失败! ")

# 需求: 提取“qq:1234567”中的qq号码
# match_obj =re.match("qq:([1-9]\d{4,11})","qq:1234567")
#判断是否有值
# if match_obj:
  #  result=match_obj.group(1)
  #  print(result)
# else:
#    print("匹配失败! ")
# 3. \num: 引用分组num匹配到的字符串
# 需求:
match_obj = re.match("<[a-z]+>.*</[a-z]+>", "<html>hh</html>")
#判断是否有值
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配失败! ")

