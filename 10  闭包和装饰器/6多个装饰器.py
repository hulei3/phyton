# 定义第一个装饰器
def make_p(func):
     def inner():
        result="<p>"+func()+"<p>"
        return result
     return inner

# 定义第二个装饰器
def make_div(func):
    def inner():
        result="<div>"+func()+"</div>"
        return result
    return inner

@make_div
@make_p
def contect():
    return"人生苦短，我学phyton"

result=contect()
print(result)
# <div><p>"人生苦短，我学phyton"</p><div>
'''
装饰的过程:有内到外的装饰过程，先去执行内部，再执行外部
原理:make_div(nake_p(contect))
'''