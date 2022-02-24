#3.7 task: вывести среднее арифметическое введенных чисел
s = input()  #вводим числа через пробел
print (s)
l1 = s.split(" ")                #добавляем разделитель
print (l1)
numbers = []                  #создаем пустой список
for i in l1:                  #добавляем каждое число в список
    numbers.append(int(i))
print (numbers)
print (sum(numbers) / len(numbers))    #выводим среднее арифметическое
