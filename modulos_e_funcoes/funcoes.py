# Defini a função
def imprime( str ):
   "Isso imprime uma string passada nesta funcao"
   print (str)
   return;

# Chama a função
imprime("Sou a primeira chamada para a funcao definida pelo usuario!")
imprime("Novamente segunda chamada para a mesma funcao")

def saudacoes(nome):
   "String da funcao saudacoes"
   print ("Hello {}".format(nome))
   return
   
saudacoes("Jimi Hendrix")
saudacoes("Eddie Van Halen")
saudacoes("Allan Holdsworth")

def adicao(x,y):
   z=x+y
   return z

a=10
b=20
resultado = adicao(a,b)
print ("a = {} b = {} a+b = {}".format(a, b, resultado))