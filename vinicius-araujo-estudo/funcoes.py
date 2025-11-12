#Funções 

#Funções são blocos de código reutilizáveis que realizam
#uma tarefa específica. Em vez de escrever o mesmo código 
#várias vezes, criamos uma função e apenas a chamamos sempre que necessário.

#Exemplo "real"
#Imagine que você tem que calcular o imposto de vários produtos em uma loja.
#Em vez de repetir a mesma coisa várias vezes, você pode criar uma função
#chamada calculae_imposto() e usá-la sempre que precisar.

# Parametros

#def saudacao(nome):
 #   print(f"Olá, {nome}! Bem-vindo ao curso de Python.")

#saudacao("Vini")

# Retorno de valores 

#def somar (a,b):
 #   return a+b

#Cgamando a função e armazenando o resultado
#resultado = somar(5,3)
#print (f"A soma é igual {resultado}")

def calcular_media(n1, n2, n3):
    media = (n1 + n2 +n3) / 3
    return media

#chamando a função
resultado = calcular_media(8,9,7)
print(f"A média é {resultado:.2f}")




