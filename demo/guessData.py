import random
times = 3
secret = random.randint(1, 10)
print('----我爱Clare-----')
guess = 0
print('不妨猜一下我现在心里想的是哪个数字吧:')

while guess != secret and times > 0:
    temp = input()
    while not temp.isdigit():
        temp = input('抱歉，您的输入有误，请输入一个整数:')
    guess = int(temp)
    times = times - 1

    if guess == secret:
        print('卧槽，你是我心里的蛔虫吗？')
        print('猜中也没有奖励')
        times = 0
    else:
        if guess > secret:
            print("哥，大了大了---")
        else:
            print('嘿，小了小了--')
        if times > 0:
            print('再试一次吧：')
        else:
            print('机会用光了')

print('游戏结束，不玩拉')


