import json

with open ('students1.json', 'r', encoding = 'utf-8') as js_file:
    students_dict = json.load (js_file)

def select (criterion, param, dict_):
    
    students_dict_copy = {}
    for st in dict_.keys ():
        students_dict_copy [st] = dict_ [st]

    for fullname in dict_.keys ():
        if dict_ [fullname][criterion] != param:
            del students_dict_copy [fullname]
    
    return students_dict_copy

while True:

    sex = input ('Какой пол у студента (м/ж)? ')

    if sex in ('м', 'муж', 'мужской'):
        students_dict = select ('gender', 'мужской', students_dict)
        break

    elif sex in ('ж', 'жен', 'женский'):
        students_dict = select ('gender', 'женский', students_dict)
        break

age = input ('Сколько студенту лет? ')
students_dict = select ('age', age, students_dict)

while True:

    fromSPb = input ('Студент из Санкт-Петербурга (да/нет)? ')

    if fromSPb in ('n', 'no', 'нет'):
        students_dict = select ('hometown', 'не Питер', students_dict)
        break
    elif fromSPb in ('y', 'yes', 'да'):
        students_dict = select ('hometown', 'Питер', students_dict)
        break

while True:

    haircol = input ('Какой цвет волос у студента: темные или светлые (1/2)? ')

    if haircol in ('1', 'темные'):        
        students_dict = select ('hair-color', 'темные', students_dict)
        break
    elif haircol in ('2', 'светлые'):
        students_dict = select ('hair-color', 'светлые', students_dict)
        break
        
while True:

    favdrink = input ('Что предпочитает студент: чай или кофе (1/2)? ')

    if favdrink in ('1', 'чай'):
        students_dict = select ('favorite-drink', 'чай', students_dict)
        break
    elif favdrink in ('2', 'кофе'):
        students_dict = select ('favorite-drink', 'кофе', students_dict)
        break

while True:

    favanim = input ('Кто больше нравится студенту: собаки или кошки (1/2)? ')

    if favanim in ('1', 'собаки'):
        students_dict = select ('favorite-animal', 'собаки', students_dict)
        break
    elif favanim in ('2', 'кошки'):
        students_dict = select ('favorite-animal', 'кошки', students_dict)
        break

while True:

    favyt = input ('Какое время года больше нравится студенту: зима или лето (1/2)? ')

    if favyt in ('1', 'зима'):
        students_dict = select ('favourite-yeartime', 'зима', students_dict)
        break
    elif favyt in ('2', 'лето'):
        students_dict = select ('favourite-yeartime', 'лето', students_dict)
        break

while True:

    favdt = input ('Что больше нравится студенту: день или ночь (1/2)? ')

    if favdt in ('1', 'день'):
        students_dict = select ('favourite-daytime', 'день', students_dict)
        break
    elif favdt in ('2', 'ночь'):
        students_dict = select ('favourite-daytime', 'ночь', students_dict)
        break

isGot = False

for student in students_dict.keys ():

    if not isGot:

        while True:

            isStud = input (f'Вы загадали студента, которого зовут {student} (да/нет)? ')

            if isStud in ('y', 'yes', 'да'):
                Stud = student
                isGot = True
                break
            elif isStud in ('n', 'no', 'нет'):
                break

    else:
        break

if not isGot:
    print ('\nНе удалось угадать студента. Проверьте правильность введенных данных и попробуйте заново.')
else:
    print (f'\nПрограмма угадала студента, которого зовут {Stud}.')