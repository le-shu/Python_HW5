# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open('code.txt', 'r') as code:
    code = code.read()

def Compdatasion(txt):
    count = 1
    data = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            data = data + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        data = data + str(count) + txt[-1]
    return data

def Recovary(txt):
    number = ''
    data = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            data = data + txt[i] * int(number)
            number = ''
    return data


s = code
print(f"Текст после кодировки: {Compdatasion(s)}")
print(f"Текст после дешифровки: {Recovary(Compdatasion(s))}")