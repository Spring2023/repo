#3.6 task: создать второй список чисел, которые встречаются не один раз в первом списке
s = input()  #вводим числа
l1 = s.split(" ")           #используем разделитель
l2 = []                      #создаем пустой список
for i in l1:                   #ищем повторяющиеся
    if l1.count(i) > 1 and i not in l2:
        l2.append(i)
print (" ".join(map(str,l2)))  #выводим результат
