# 递归特点:1 函数内部调节自己 2 必须有出口
# 回顾函数返回值:写法和返回的位置:函数调用的位置
# def return_num():
 #    return 100

# result=return_num()
# print(result)

# 需求:3以内的数字累加和，3+2+1=6
# 6=3+2以内的数字累加和
# 2以内的数字累加和=1+1数字以内的累加和
# 1 以内的数字类加和=1  # 这就是出口
def sum_numbers(num):
  # 写出口，返回值是1
    if num==1:
      return 1
  # 当前数字累加+（当前数字累加-1）的累加和
    return num +sum_numbers(num-1)

result=sum_numbers(3)
print(result)
# 如果没有出口会报错，超出最大递归深度

