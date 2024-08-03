import math
a = int(input('请输入第一个直角边长:'))
b = int(input('请输入第二个直角边长:'))

m=a*a+a+b+b*b
c= math.sqrt(m)
print(f"直角三角形斜边长为: {c}")