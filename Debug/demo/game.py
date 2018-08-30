import random
a = random.randint(1,9)
guess = int(input("请输入一个数值，与改随机数比较："))

while guess != a:
    if guess > a:
        print("大了")
    elif guess < a:
        print("小了")
    guess = int(input("猜错了，再给你一次机会："))

    if guess == a:
        print("你真厉害，猜对了")
    else:
        if guess > a:
            print("你猜大了")
        else:
            print("你猜小了")
print("游戏结束")