#     Работас файлами

# № 1

# with open('text.txt', 'w', encoding = 'utf-8') as myfile: # открой файл 'text.txt', запииши в него - команда 'w, кодкодировкой - utf-8; результат назвать переменной f
#     myfile.write('Hello, world!\n')
#     myfile.write('\tеще раз')
#


# № 2 чтение и вывод
#
# with open('text.txt', 'r', encoding = 'utf-8') as myfile:
#     text = myfile.read()
#     print(text)


# № 3 Чтение файла построчно - лучший вариант для чтения - ест меньше памяти для больших текстов

with open('text.txt', 'r', encoding = 'utf-8') as f:
    for line in f:
        line = line.upper()
        line = line.replace("\n", "") # заменяем перевод строки на пустоту
        print(line)