# 递归特点:=函数内部自己调自己 2必须有出口
# 回顾函数返回值:写法和返回的位置:函数调用的位置
# def return_num():
#      return 100

# result = return_num()
# print(result)

# 需求:3以内的数字累加和，3+2+1=6
# 6=3+2数字以内的和累加
# 2以内的数字累加和 =2+1以内的数字累加和
# 1以内的数字累加和=1    #这就是入口

def sum_numbers(num):
    # 2 写出口，如果是1，直接返回1
    if num==1:
        return 1
    # 如果不是1，重复职行累加和并返回结果
    # 1.当前数字+（当前数字-1）的累加和
    return num+sum_numbers(num-1)

result = sum_numbers(3)
print(result)
 # 如果没有出口，会报错，超出最大递归深度