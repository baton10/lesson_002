# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв а в слове
word = 'Архангельск'
print(len(word))





# Вывести количество гласных букв в слове

vowels = 'аеёиоуыэюя' #  предлагают решать через vowels = u'аеёиоуыэюя'. u - unicode. Преобразование строки в u
word = 'Архангельск'
vowels = sum(1 for text in word.lower() if text in vowels)
print(vowels)







# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))



# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
sentence = sentence.split(' ')
print(sentence[0][0])
print(sentence[1][0])
print(sentence[2][0])
print(sentence[3][0]) # написать оптимальнее с циклом, типа мы не знаем кол-во слов


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
# ???
