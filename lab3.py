alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

msg_input = input('Введите сообщение для шифровки на кириллице: ').lower()
step = (int(input('Введите шаг шифровки от 1 до 33: ')))
msg_output ='' 

for i in msg_input:
    letter_place = alphabet.find(i)
    new_letter_place = letter_place + step
    if i in alphabet:
        msg_output += alphabet[new_letter_place % len(alphabet)]
    else:
        msg_output += i 

print(msg_output)

 
