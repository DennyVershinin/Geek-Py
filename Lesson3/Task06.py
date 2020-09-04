def capitalize_func(word):
    word = word.capitalize()
    return word


sentence = input('Введите предложение ')
sentence = sentence.split()
res = ''

for s in sentence:
    res = res + ' '+ capitalize_func(s)

print(res)
