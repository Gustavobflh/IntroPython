import math
def newton_aprox(n):
    dif = 1
    aprox=n/2
    while dif > 0.0001:
        melhor = (aprox + n/aprox)/2
        dif = melhor - aprox
        if dif < 0:
            dif = dif*(-1)
        aprox = melhor
        print(melhor)
    

k=int(input('Raiz quadrada de \n'))   

newton_aprox(k)

print("Comparacao")
print(math.sqrt(k))
