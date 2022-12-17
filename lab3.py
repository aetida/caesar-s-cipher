alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' #переменная содержащая алфавит

#обработка корректности выбора действия
while True:
    try:
        select_act = int(input('Выберите действие \n [1] Зашифровать сообщение \n [2] Расшифровать сообщение \n'))

        if select_act != 1 and select_act != 2:
            print(' некорректный ввод \n повторите ввод еще раз')
        else:
            break
    except ValueError:
        print('Ошибка ввода. Попробуйте еще раз')

#обработка корректности выбора шага шифрования
while True:
    try:
        step = (int(input('Введите шаг шифровки от 1 до 33: ')))
        if step > 33 or step < 1:
            print(' некорректный ввод \n повторите ввод еще раз')
        else:
            break
    except ValueError:
        print('Ошибка ввода. Попробуйте еще раз')


msg_input = input('Введите сообщение для шифровки на кириллице: ').lower() #запрос сообщения и преобразование в нижний регистр
msg_output =''  #переменная для выходного сообщения

#преобразовния шага для дешифровки
if select_act == 2: 
    step = step*(-1)
else:
    pass

#блок шифрования
for i in msg_input: #цикл обращения к каждому символу
    letter_place = alphabet.find(i) #поиск местоположения в переменной alphabet символа i из сообщения
    new_letter_place = letter_place + step #к индексу добавляется шаг
    if i in alphabet:
        msg_output += alphabet[new_letter_place % len(alphabet)] #добавление буквы в переменную для вывода
    else:
        msg_output += i #проуск символов не из русского алфавита

print(msg_output) #вывод зашифрованного/дешифрованного сообщения

 
