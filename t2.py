import os

# Путь к исходому файлу
path = os.path.abspath('test.txt')
# Чтение и запись массивов строк в наш  исходный массив
f = open(path, 'r')

file = f.readlines()
massiv = []

for i in file:
    massiv.append(i.replace('\n', '').split())
f.close()


# Начальное задание переменной первым массивом строк нашего массива
testArr = massiv[0]
# Выходной массив
flowArr = []
# Промежуточные массивы 
a = []
b = []

while len(massiv) != 0:
    for i in massiv:
        # Если первый или второй элемент массива равные третьему элементу итерации
        if testArr[0] == i[2] or testArr[1] == i[2]:
            # Что-бы каждый раз не засовывать начальный testArr при захождении в эту ветку
            if len(a) == 0:
                a.append(testArr)
            testArr = i
            a.append(testArr)
            break
    # Сработает если пройду весь цикл без 'break', 
    # то есть у массива не совпадут элементы, 
    # что значит что он независит от других
    else:
        # Проверяем есть ли в массиве 'a' что-то, 
        # если да, значит другие массивы зависимо от текущего массива
        if len(a) != 0:
            # Тогда вытаскиваю все подмассивы из 'a' в 'b' и 
            # удаляю их из изначального массива
            for j in a:
                b.append(j)
                massiv.remove(j)
            # Запихиваю весь массив 'b' в конечный массив, 
            # теперь он как отдельный поток
            # и обнуляю промежуточные массивы
            flowArr.append(b)
            a = []
            b = []
            # Проверка на то что в массиве еще остались элементы
            if len(massiv) != 0:
                testArr = massiv[0]
            else: testArr = 0
        else:
            # Если 'a' пуст, значит наш массив независим от других массивов 
            # И другие массивы не зависимы от него 
            # полностью выделяем его в отдельный поток и удаляем из исходного массива
            flowArr.append(testArr)
            massiv.remove(testArr)
            # Проверка на то что в массиве еще остались элементы
            if len(massiv) != 0:
                testArr = massiv[0]
            else: testArr = 0

# Требуется для определения степени загрузки 
# (тут находим максимальный по длине действий поток)
maxLen = 1
for i in flowArr:
    if len(i) > maxLen:
        maxLen = len(i)


# Путь для выходного файла
path2 = os.path.abspath('conclusion.txt')

# Его обработка и сохранение
with open(path2, 'w') as f2:
    for i in range(len(flowArr)):
        if type(flowArr[i][0]) == str: 
            percent = 1  / maxLen * 100
        else:
            percent = len(flowArr[i])  / maxLen * 100
        f2.write(f'{i+1}: {flowArr[i]} : Степень загрузки = {percent}%\n')