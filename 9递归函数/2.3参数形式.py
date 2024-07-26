#  需求:引用是否可以当做实参传入人惨
def test1(a):
    print(a)
    print(id(a))

    a+=a  # 等价 a=a+a
    print(a)
    print(id(a))

# b=10
# test1(b)

c=[11,22]
test1(c)