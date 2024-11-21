""" A Sociedade Brasileira de Computação (SBC) vai instalar uma nova máquina de café expresso 
em seu prédio de 3 andares. Cada funcionário bebe 1 café por dia e precisa subir ou descer 
escadas até o andar onde a máquina estiver. Como cada andar leva 1 minuto para ser percorrido, 
a presidência quer minimizar o tempo total gasto pelos funcionários indo e voltando. 

O problema é calcular o tempo mínimo total considerando o número de funcionários em cada andar 
(A1, A2, A3). 
O output deve ser o menor tempo possível para a melhor localização da máquina. """

a1 = int(input())
a2 = int(input())
a3 = int(input())
 
#Para a maquina nos andares 1, 2 e 3
tAndar1 =  (a2 * 2) + (a3 * 4)
tAndar2 = (a1 * 2) + (a3 * 2)
tAndar3 = (a1 * 4) + (a2 * 2)
 
if tAndar1 <= tAndar2 and tAndar1 <= tAndar3:
    print(tAndar1)
elif tAndar2 <= tAndar1 and tAndar2 <= tAndar3:
    print(tAndar2)
elif tAndar3 <= tAndar1 and tAndar3 <= tAndar2:
    print(tAndar3)