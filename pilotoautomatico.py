""" Uma fábrica de carros elétricos precisa de um programa para decidir se um carro B, 
posicionado entre dois carros A e C, deve acelerar, desacelerar ou manter sua velocidade. 
A decisão é baseada nas distâncias entre as traseiras dos carros:

- **Acelerar**: se a distância entre B e A for menor que a distância entre C e B.
- **Desacelerar**: se a distância entre B e A for maior que a distância entre C e B.
- **Manter velocidade**: se as duas distâncias forem iguais.

Input: Três números inteiros, A, B e C (representando as posições das traseiras 
dos carros, com \( 0 \leq A < B < C \leq 500 \)).

Output: Um número inteiro:
- `1` para acelerar,
- `-1` para desacelerar,
- `0` para manter a velocidade. """

a = int(input())
b = int(input())
c = int(input())
 
distanciaAB = b - a
distanciaBC = c - b
 
#Veerificando se as distancias sao iguais independente do sinal
if distanciaAB < 0:
    if (distanciaAB * -1) == distanciaBC:
        print(0)
        quit()
if distanciaBC < 0:
    if (distanciaBC * -1) == distanciaAB:
        print(0)
        quit()
 
 
if distanciaAB == distanciaBC:
    print(0)
elif distanciaAB < distanciaBC:
    print(1)
else:
    print(-1)