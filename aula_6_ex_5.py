import turtle             # nos permite usar as tartarugas (turtles)

jn = turtle.Screen()      # Abre uma janela onde as tartarugas vão caminhar
arrow = turtle.Turtle()    # Cria uma tartaruga, atribui a joana
arrow.pensize(5)

for i in [0,1,2,3,4]:
	arrow.forward(100)
	arrow.left(-144)  
