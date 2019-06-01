with open('referat.txt', 'r', encoding = 'utf-8') as f:
    text = f.read()

print(len(text)) # длина строки

words = text.split() # почему не text.split(" ") ?
print(len(words))

with open('referat_02.txt', 'a', encoding='utf-8') as f:
    all_text = text.replace(".", "!") # заменяем точки на воскл. знак
    all_text = f.write(all_text)
    print(all_text)
