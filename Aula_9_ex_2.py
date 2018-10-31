#Corredor

v_km_h = 12

v_km_min = v_km_h/60


def accel():

	v_f = 15/60

	dist_acc = 0.2 

	acceleration = v_f**2/(dist_acc*2)

	return(acceleration)

distancias = []

cont = 0

dist = 0

cont_tempo = 0
 
distancias.append(cont)

while dist <= 7:

	if dist <= 5:

		cont_tempo = cont_tempo + 1
		dist = dist + v_km_min	 
		distancias.append(dist)
	
	if dist > 5 and dist < 5.2:
		
		cont_tempo = cont_tempo + 1
		
		v_f = v_km_min +  accel()
		
		v_med = (v_km_min + v_f) 
		
		v_km_min = v_f
	
		dist = dist + v_med

		distancias.append(dist)

	if dist >= 5.2:

		cont_tempo = cont_tempo + 1
		dist = dist + v_km_min	 
		distancias.append(dist)
		 
		
		 

n = len(distancias)
for i in range(n):
    print(distancias[i])

