#3.4 task: создать список с уникальными значениями
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]  #дан список
new_list = []                #создаем пустой список
for i in my_list:
    if i in new_list:           #проверяем есть ли значение в списке
        continue
    else:
        new_list.append(i)      #добавляем уникальные значения в новый список
print ("The list with unique elements only:", new_list)  #выводим результат
