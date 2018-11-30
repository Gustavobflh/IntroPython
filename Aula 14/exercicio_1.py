# Ler colunas dee umm arquivo e acessar as colunas

def ler_arquivo(nome):
 	
   lista_coluna = []	
   colunas = {}

   
   arq = open(nome + '.txt')
   
   linhas = arq.readlines()
   n = linhas[0].strip().split()
   print(n)
   try:
      float(n[0])
      for i in range(1,len(n)+1):
          for line in linhas:

              column = line.strip().split()
              print(column)
              k = len(column)
      
              lista_coluna.append(column[i-1])

          colunas[i] = lista_coluna
          lista_coluna = []    
   except:
       linhas.pop(0)
       cont = 0
       for i in n:
           
          cont = cont+1
          for line in linhas:

             column = line.strip().split()
             print(column)
             k = len(column)
      
             lista_coluna.append(column[cont-1])

          colunas[i] = lista_coluna
          lista_coluna = [] 

   return(colunas)
   

	
   
       

print(ler_arquivo(str(input('Digite o nome do arquivo que deseja abrir: '))))


