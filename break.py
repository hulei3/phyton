# break:当某个条件成立，退出整个循环
# 需求：循环5个苹果，吃掉三个苹果，第四个和第五个不吃了
i = 1
while i<=5:
# 条件：如果吃到 4 或>3 打印吃饱了不吃
 if i==4:
    print("吃饱，了不吃了")
    break
 print(f"吃到了{i}个苹果!")
 i+=1