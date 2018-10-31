#Corredor

import matplotlib.pyplot as plt

v_km_h = 12

v_km_min = v_km_h/60

distancias = []

tempo = []

cont_dist = 0

cont_tempo = 0 

distancias.append(cont)

while dist <= 5:

	cont_tempo = cont_tempo + 1
	dist = dist + v_km_min	 
	distancias.append(cont)

n = len(distancias)
for i in range(n):
    print(distancias[i])

plt.plot(cont_tempo, dist)
plt.xlabel("tempo min")
plt.ylabel("distância km")
