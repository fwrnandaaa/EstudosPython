quantnum = int(input())
lista = []

while quantnum > len(lista):  
    lista = list(map(int, input().split()))
    
 #Media
media = sum(lista)
media = media / quantnum

#Num abaixo
numeros_abaixo = 0
for i in range(len(lista)):
    if lista[i] < media:
        numeros_abaixo = numeros_abaixo + 1
    
#Num acima
numeros_acima = 0
for i in range(len(lista)):
     if lista[i] >= media:
        numeros_acima = numeros_acima + 1
        

print(round(media, 1))
print(numeros_abaixo)
print(numeros_acima)


