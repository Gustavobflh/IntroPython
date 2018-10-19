import turtle             # nos permite usar as tartarugas (turtles)

jn = turtle.Screen()      # Abre uma janela onde as tartarugas vão caminhar
joana = turtle.Turtle()    # Cria uma tartaruga, atribui a joana
joana.shape("turtle")
joana.speed('slowest')

for i in [0,1,2,3]:
	joana.forward(50)
	joana.left(90)        
