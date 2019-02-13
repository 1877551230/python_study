def factorial(n):
    result = n
    for i in range(1,n):
        result *= i
        
    return result
number = int(input('请输入数'))
result = factorial(number)
print("%d的阶乘是：%d" % (number,result))
------------------------------------------------
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

number = int(input('请输入数字'))
result = factorial(number)
print("%d的阶乘是%d" % (number,result))
