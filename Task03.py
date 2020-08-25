n = int(input("Введите целое число\n"))
nn = int(f'{n}{n}')
nnn = int(f'{n}{n}{n}')
sum = n+nn+nnn
print("{}+{}+{}={}".format(n,nn,nnn,sum))