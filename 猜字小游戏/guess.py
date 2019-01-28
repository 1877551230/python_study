import random
print("----------------------------miracle-----------------------")
secret=random.randint(0,100)
temp = input("你猜猜我心里想的是哪个数字:")
while temp.isdigit() == False:
    print("这不是一个数字\n")
    temp = input("重新输入一个数字")
guess = int(temp)
while guess != secret:
    if guess >secret:
        print("大了")
    else:
        print("小了")
    temp = input("再猜")
    guess = int(temp)
if guess == secret:
    print("猜对了")
    print("游戏结束")    
