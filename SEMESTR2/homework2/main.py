import muldiv
import crc

while True:
    print("Выберите алгоритм хэширования: 1 - деление, 2 - умножение, 3 - CRC-32, 4 - MD5: ")
    choose_algo = int(input())
    if choose_algo in range(1, 5):
        input_string = input("Введите вашу строку: ")
        if choose_algo == 1:
            input_ords = muldiv.strOrd(input_string)
            result = muldiv.divHash(input_ords)
        elif choose_algo == 2:
            input_ords = muldiv.strOrd(input_string)
            result = muldiv.mulHash(input_ords)
        elif choose_algo == 3:
            result = crc.encodeCRC(input_string)
            
        print("Result:", result)
        break