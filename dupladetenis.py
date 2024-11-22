""" Quatro amigos querem formar duplas para jogar tênis. Cada um tem um nível de jogo 
representado por um número inteiro, e o objetivo é formar dois times com níveis de 
jogo o mais equilibrados possível. O nível de um time é a soma dos níveis dos dois jogadores.

Tarefa: Determinar a menor diferença possível entre os níveis dos dois times. """

a = int(input())
b = int(input())
c = int(input())
d = int(input())
 
ab = a + b
cd = c + d
 
if ab == cd:
    diferenca1 = 0
elif ab > cd:
    diferenca1 = ab - cd
else: 
    diferenca1 = cd - ab
 
ac = a + c
db = d + b
 
if ac == db:
    diferenca2 = 0
elif ac > db:
    diferenca2 = ac - db
else: 
    diferenca2 = db - ac
 
ad = a + d
cb = c + b
 
if ad == cb:
    diferenca3 = 0
elif ad > cb:
    diferenca3 = ad - cb
else: 
    diferenca3 = cb - ad
 
if diferenca1 <= diferenca2 and diferenca1 <= diferenca3:
    print(diferenca1)
elif diferenca2 <= diferenca1 and diferenca2 <= diferenca3:
    print(diferenca2)
else:
    print(diferenca3)