#Projeto 1
#Pêndulo elastico




from math import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

g = 9.8

#Caracteristicas do pendulo
print('Informe as características do sistema')
k = float(input('Constânte da mola em N/m:'))
m = float(input('Massa do pendulo em kg:'))
L = float(input('Comprimento natural da mola em metro:'))


#posiao inicial em dadas pelo angulo e comprimento inicial
print('Informe ascoordenadas da posição inicial do pêndulo ')
r  = float(input('Comprimento inicial da mola: '))
dif = sqrt((L-r)**2)
while dif >= L:
	print('Se a diferença entre o comprimento natural e inicial da mola for maior que o comprimento natural, talvez o programa não funcione')
	r  = float(input('Por favor, digite outro comprimento inicial da mola: '))
	dif = sqrt((L-r)**2)

theta = radians(float(input('Angulo inicial: ')))

#tempo total
delta_t = 0.0025
time = int(input('informe o tempo em segundos:'))

n = time//delta_t
n = int(n)

#precisão
p = 1001
while p > 1000 or p < 0:
        
    p = 10**int(input('Informe a precisãodo programa de 0 à 3.'
                      'OBS: Dependendo do tempo total e da precisão '
                      'o programa demora um pouco para rodar''\n',))

    
#definindo as listas
position_rad = []
position_theta = []
position_x = []
position_z = []
list_time = [0]
list_v = [0] # para o gráfico módulos de v vs t
list_v_x = [0]
list_v_z = [0]
acceleration = []
acceleration_x = []
acceleration_z = []
Energy = []

#Colocando o primeiro item das listas
position_rad.append(r)
position_theta.append(degrees(theta))
position_x.append(r*sin(theta))
position_z.append(r*cos(theta))


#função para criar arquivos de saída
def bloco(nome, dado, a):
    dado = str(dado)
    arquivo = open(nome + '.txt', a)
    arquivo.write(dado + '\n')
    arquivo.close()
    
names = ['time','position_x','position_z','velocity_x','velocity_z','acceleration_x','acceleration_z']
for j in range(len(names)):
    bloco(names[j],names[j], 'w')



#contador do tempo
def time_up(t):
    cont_time = 0
    for i in range(n):
        cont_time = cont_time + t
        list_time.append(round(cont_time,5))
    
#função de atualização em coord. polar            
def runnig_values(r, theta, L):

    #adicionando algumas condições iniciais alis
    
    v_rad = 0    
    v_ang = 0
    
    acc = sqrt((- g*sin(theta)/r)**2 + (-k*(r-L)/m + g*cos(theta))**2)
    acceleration.append(acc) # aceleração inicial
    acceleration_x.append(acc*sin(theta))
    acceleration_z.append(acc*cos(theta))
    
    E_mec = -m*g*r*cos(theta)+ (k*(r-L)**2)/2 # energia inicial
    Energy.append(E_mec) # energia inicial

    
    for i in range(n):
        for i in range(p):#dois "for" para aumentar a precisão
            #Caso qeiram deixar o programa mais rápido, apenas diminua o valor
            #de p, se quiser deixar mais preciso, aumente
            #Atualização da posição angular
            acc_ang = - g*sin(theta)/r - 2*v_ang*v_rad/r
            v_ang = v_ang +  acc_ang*delta_t/p
            theta = theta + v_ang*delta_t/p
            


            #atualização da posição no eixo r
            acc_rad = -k*(r-L)/m + g*cos(theta) + (v_ang**2)*r
            v_rad = v_rad + acc_rad*delta_t/p
            r = r + v_rad*delta_t/p

            
            
        
        
        #passando para cartesiano
        acc = sqrt((acc_ang*r)**2 + acc_rad**2)
        v_mod = sqrt(v_rad**2 + (r*v_ang)**2)
        v_x = v_ang*r*cos(theta) - v_rad*sin(theta)
        v_z = v_rad*cos(theta) - v_ang*r*sin(theta)
        x = r*sin(theta)
        z = r*cos(theta)
        acc_x = acc*sin(theta)
        acc_z = acc_rad*cos(theta) - acc_ang*r*sin(theta)

        
        E_mec = (m*v_mod**2)/2 - m*g*r*cos(theta) + (k*(r-L)**2)/2
        #A energia se conserva pois permanece aproximadamente constante
        #As pequenas oscilações na ordem de 10^-3
        #são devido ao erro da integraçã numérica
        
       #Adicionando os itens às respectivas listas
        position_x.append(round(x,5))
        position_z.append(round(z,5))
        list_v.append(round(v_mod,5))
        list_v_x.append(round(v_x,5))
        list_v_z.append(round(v_z,5))
        acceleration.append(round(acc,5))
        acceleration_x.append(round(acc_x,5))
        acceleration_z.append(round(acc_z,5))
        position_rad.append(round(r,5))
        Energy.append(round(E_mec,5))



runnig_values(r, theta, L)
time_up(delta_t)


#fazendo os gráficos
logical_graf = input('Deseja abrir os gráficos? Digite s ou n' '\n')
if logical_graf == 's':
         
    def grafic(x,y,lab_x,lab_y):
        plt.plot(x,y)
        plt.xlabel(lab_x)
        plt.ylabel(lab_y)
        plt.show()
    grafic(position_x, position_z ,'posição x em m','Posição z em m' )
    grafic(list_time, Energy , 'tempo s','Energia mecanica' )
    grafic(list_time, position_rad , 'tempo s','Comprimento em m' )
    grafic(list_time, list_v ,"tempo s",'vocidade m/s' )
    grafic(list_time, acceleration, 'tempo s',' aceleracao m/s^2')
    grafic(position_x, list_v_x ,'posicao x (metro)','velocidade no eixo x m/s' )
    grafic(position_z, list_v_z ,'posicao z (metro)','velocidade no eixo z m/s' )

#Criando arquivos de saída
logical_arq = input('Deseja criar arquivos de saída para os dados? Digite s ou n' '\n')
if logical_arq == 's':
    ll = [list_time, position_x,
            position_z,
            list_v_x,
            list_v_z,
            acceleration_x, acceleration_z]

    l_label = ['time','position_x', 'position_z',
               'velocity_x', 'velocity_z', 'acceleration_x',
               'acceleration_z']
    
    for j in range(len(l_label)):
        for i in range(len(list_time)):
             bloco(l_label[j], ll[j][i], 'a')
    

#Animação do pêndulo
logical_ani = input('Deseja abrir a simulação? Digite s ou n' '\n')
if logical_ani == 's':

    fig, ax = plt.subplots()
    xdata, ydata = position_x, position_z
    ln, = plt.plot([], [], 'ro', animated = True)
    spring, = plt.plot([], [], 'b-', linewidth = 2)



    def init():
        ax.set_xlim(-2*L, 2*L)
        ax.set_ylim(2*r,0)
        return ln,

    def draw(n):
        spring.set_data([ 0.0, xdata[n] ], [ 0.0,  ydata[n] ])
        ln.set_data(xdata[n], ydata[n])
        return spring,ln

    ani = FuncAnimation(fig, draw, n, interval= 0.001,
                    init_func=init, blit=True)
    plt.show()
