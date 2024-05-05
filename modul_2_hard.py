rezult = []
while 1 > 0:
    def inp_ut(x):
        while True:
            try:
                text = '{} {} {} '.format("Введите, пожалуйста,число", x, '>>>')
                x = int(input("введите число от 3 до 20: "))
                return x
            except ValueError:
                print("Некорректный ввод, пожалуйста введите число от 3 до 20")
    n = inp_ut('n')
    if n <= 20 and n >= 3:
        for i in range(1, 21):
            for j in range(1, 21):
                if n % (i + j) == 0 and (i + j) <= n and i != j and i < j:
                    rezult.extend((i, j))
    else:
        print("Некорректный ввод, пожалуйста введите число от 3 до 20")
    print(*rezult)
    rezult = []