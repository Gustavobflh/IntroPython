import math
cateto_oposto = 4
cateto_adjacente = 2 
tangente_theta = cateto_oposto/cateto_adjacente
theta  = math.atan(tangente_theta)
print(theta, 'em radianos')

theta2 = math.degrees(math.acos(math.sqrt(2)/2))
print(theta2, 'graus')

def poema():

    print('caminante, no hay camino,')
    print('se hace camino al andar.')
    
print(poema)

poema()

def verso_poema():
    print('Caminante, son tus huellas')
    print('el camino y nada más;')
    
    poema()
    
    print('Al andar se hace el camino,')
    print('y al volver la vista atrás,')
    print('se ve la senda que nunca')
    print('se ha de volver a pisar.')
    print('Caminante no hay camino')
    print('sino estelas en la mar.')

