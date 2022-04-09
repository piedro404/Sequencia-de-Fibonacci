n1 = (int(input("Informe o Primeiro Número: ")))
n2 = (int(input("Informe o Segundo Número: ")))
g = (int(input("Informe o Número de Gerações: ")))
lista=[]
listao=[]
lista.append(n1)
lista.append(n2)
for i in range(1,g-1):
    listao.append(n2/n1)
    ns = n1+n2
    lista.append(ns)
    n1 = n2
    n2 = ns
print(f"Sêquencia\n{lista}")
print(f"Número de ouro\n{listao}")
