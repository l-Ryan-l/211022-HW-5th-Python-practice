# # 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

# Вариант 1
text = str(input())
text = text.split()
result = []
for i in text:
    if 'абв' not in i:
        result.append(i)
print(result)

# Вариант 2
text = str(input())
text = text.split()
result = list(filter(lambda x: 'абв' not in x, text))
print(result)


# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('rle_data.txt', 'w') as data:
    data.write('aaaaaabbbccccddddd')
with open('rle_data.txt', 'r', encoding='utf-8') as dt:
    data = list(map(str, dt.read()))

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res

print(f'Результат сжатия:  {coding(data)}')
print(f'Результат восстновления: {decoding(coding(data))}')