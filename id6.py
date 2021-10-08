try:
    amount = int(input("Сколько чисел вы хотите:"))
except ValueError:
    print("Ошибка!")
else:
    array = []
    count = 0
    try:
        while count != amount:
            a = int(input("Вводите числа:"))
            array.append(a)
            count += 1
    except ValueError:
        print("Ошибка!")
    else:
        try:        
            delta = int(input("Введите разницу:"))
        except ValueError:
            print("Ошибка!")
        else:    
            min_value = min(array)
            result = 0
            for b in array:
                if b - min_value == delta:
                    result += 1
            print("Количество чисел, отличающихся от минимального на",delta,":",result)



