#Projeto 1
#Pêndulo simples

from math import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

g = 9.8

#Caracteristicas do pendulo
print('Informe as características do sistema')
r = float(input('Comprimento do pendulo:'))
m = float(input('Massa do pendulo em kg:'))

#posiao inicial em dadas pelo angulo e comprimento inicial
print('Informe ascoordenadas da posição inicial do pêndulo ')
theta = radians(float(input('Angulo inicial: ')))



#tempo total
delta_t = 0.00625
time = int(input('informe o tempo em segundos:'))

n = time*160

#definindo as listas
position_r = []
position_x = []
position_z = []
list_time = [0]
list_v = [0] # para o gráfico módulos de v vs t
list_v_x = [0]
list_v_z = [0]
acceleration = []
Energy = []
#Colocando o primeiro item das listas

position_r.append(r)
position_x.append(r*sin(theta))
position_z.append(r*cos(theta))


#função para criar arquivos de saída
def bloco(nome,dado):
    dado = str(dado)
    arquivo = open(nome + '.txt', 'a')
    arquivo.write(dado + '\n')
    arquivo.close
    
names = ['time','position_x','position_z','velocity_x','velocity_z','acceleration_x','acceleration_z']

for j in range(len(names)):
    if names[j] == 'time' or names[j] == 'velocity_x' or names[j] == 'velocity_z':
        bloco(names[j],0)

bloco('position_x', r*sin(theta))
bloco('position_z', r*sin(theta))

#contador do tempo
def time_app(t):
    cont_time = 0
    for i in range(n):
        cont_time = cont_time + t
        list_time.append(cont_time)
    
#função de atualização em coord. polar            
def vel(r, theta):

    vel_tan = 0
    acc = sqrt((g*sin(theta))**2)
    acceleration.append(acc) # aceleração inicial
    bloco('acceleration_x', acc*sin(theta))
    bloco('acceleration_z', acc*sin(theta))
    theta_i = theta
    E_mec =  -m*r*g*cos(theta)
    Energy.append(E_mec)
    p = 10**3
    for i in range(n):
        for i in range(p): # dois for para melhorar a precisão do programa
            #Atualização da posição angular
            acc_tan = - g*sin(theta)
            vel_tan = vel_tan + acc_tan*delta_t/p
            vel_ang = vel_tan/r
            theta = theta + vel_ang*delta_t/p
        
            
        #passando para cartesiano
        acc = sqrt((g*sin(theta))**2)
        v_mod = sqrt(vel_tan**2)
        v_x = v_mod*sin(theta)
        v_z = v_mod*cos(theta)
        x = r*sin(theta)
        z = r*cos(theta)
   
        E_mec = (m*v_mod**2)/2 - m*r*g*cos(theta)

        #fazendo os gráficos pedidos
        position_x.append(x)
        position_z.append(z)
        list_v.append(v_mod)
        list_v_x.append(v_x)
        list_v_z.append(v_z)
        acceleration.append(acc)
        position_r.append(r)  
        Energy.append(E_mec)
        
        #adicionando os valores nos blocos de nota
        bloco('position_x', x)
        bloco('position_z', y)
        bloco('velocity_x', v_x)
        bloco('velocity_z', v_z)
        bloco('acceleration_x', acc*sin(theta))
        bloco('acceleration_z', acc*cos(theta))
        
def grafic(x,y,lab_x,lab_y):
    plt.plot(x,y)
    plt.xlabel(lab_x)
    plt.ylabel(lab_y)
    plt.show()
    

        
time_app(delta_t)
vel(r, theta)
grafic(list_time, Energy , 'tempo s','Energia mecanica' )
grafic(list_time, position_r , 'tempo s','comprimento em m' )
grafic(list_time, list_v ,"tempo s",'velocidade m/s' )
grafic(list_time, acceleration, 'tempo s',' aceleracao m/s^2')
grafic(position_x, list_v_x ,'posicao x (metro)','velocidade m/s' )
grafic(position_z, list_v_z ,'posicao z (metro)','velocidade m/s' )







#Animação do pêndulo
logical = input('Deseja abrir a simulação? Digite s ou n' '\n')
if logical == 's':

    fig, ax = plt.subplots()
    xdata, ydata = position_x, position_z
    ln, = plt.plot([], [], 'ro', animated = True)
    spring, = plt.plot([], [], 'b-', linewidth = 2)



    def init():
        ax.set_xlim(-2*r, 2*r)
        ax.set_ylim(2*r,0)
        return ln,

    def update(n):
        spring.set_data([ 0.0, xdata[n] ], [ 0.0,  ydata[n] ])
        ln.set_data(xdata[n], ydata[n])
        return spring,ln

    ani = FuncAnimation(fig, update,n, interval= 0.001,
                    init_func=init, blit=True)
    plt.show()
