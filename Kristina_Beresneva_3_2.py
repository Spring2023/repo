#3.2 task: создать список участников группы и добавлять/удалять их
beatles = []           #создать пустой список
print (beatles)        #вывести пустой список
beatles.append ("JohnLennon")   #добавить в пустой список
beatles.append ("Paul McCartney")
beatles.append ("George Harrison")
print (beatles)          #вывести новый список
for i in range (2):
    beatles.append (str(input("Введите имя: "))) #добавить еще участников
print (beatles)
del beatles [3: 5]     #удалить двух последних
print (beatles)
beatles.insert (0, "Ringo Starr")  #вставить нового участника в начало списка
print (beatles)
print (len(beatles), type(beatles))  #вывести длину списка и тип
