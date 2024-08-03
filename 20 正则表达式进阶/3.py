import re

# 贪婪模式:尽可能匹配更多
# match_obj=re.match("ab*c","abbbbbbbc")
# print(match_obj.group())

# 非贪婪模式:尽可能匹配最少，?修饰的是*，如果说?后面有字符，那么取的是后面的字符的最少
match_obj=re.match("ab*?c","abbbbc")
print(match_obj.group())