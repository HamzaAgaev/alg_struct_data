def strOrd(string: str) -> list:                # строка -> коды букв
    ords = []
    for s in string:
        ords.append(ord(s))
    return ords

CONST_ = (5 ** 0.5 - 1) / 2

def mulHash(mularray: list) -> list:            # метод умножения
    m = len(mularray)
    hashes = []
    for k in mularray:
        hash_ = int(m * ((k * CONST_) % 1))     # дробная часть умножения ключа на константу, умноженная на длину массива
        hashes.append(hash_)    
    return hashes

def divHash(divarray: list) -> list:            # метод деления
    m = len(divarray)
    hashes = []
    for k in divarray:
        hash_ = k % m                           # деление по остатку
        hashes.append(hash_)
    return hashes