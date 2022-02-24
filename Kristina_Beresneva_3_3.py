#3.3 task: отсортировать список
n = int(input("Введите количество чисел: "))  #спрашиваем количество чисел
list = []                                   #создаем пустой список

if n > 0:                                  
    for i in range(n):
        a = int(input("Введите число: "))   #спрашиваем число
        list.append (a)                     #добавляем число в список
    print (list)                            #выводим список

swapped = True

while swapped:                            #сортируем список
    swapped = False
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            swapped = True
            list[i], list[i + 1] = list[i + 1], list[i]        
print (list)                            #выводим готовый список
list.sort()                             #пробуем готовую функцию
print (list)
