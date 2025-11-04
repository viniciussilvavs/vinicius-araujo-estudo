# Lista
#Definidas entre colchetes [] e pode armazenar diferentes tipos dados.

#frutas = ["maçã", "banana", "laranja"]
#numeros = [1, 2, 3, 4, 5]
#misturada = ("python", 3.14, True)

#Acessando elementos da lista

#print (frutas[0]) #maçã
#print (frutas[1]) #banana
#print (frutas[2]) #laranja
#print (frutas[-1]) #laranja (índice negativo conta de trás para frente)

#Alterando um valor na lista
#print (frutas)

#frutas[1] = "uva"
#print (frutas) # ("maçã", "uva", "laranja")

#Adicionando elementos à lista

#append(): adiciona um intem ao final
#insert(): adiciona um ítem em uma posição específica

#numeros = [1, 2, 3]
#print(numeros)

#numeros.append(4)
#print(numeros)   #[1,2,3,4]

#numeros.insert(1, 10) #(posição, valor)
#print(numeros) # [1, 10, 2, 3, 4]  (inseriu o 10 na posição 1)

#Removendo elementos da lista

#remove(): remove um item pelo valor
#pop():  remove um item pelo índice (ou o último item se nenhum índice for passado)


#frutas = ["maçã", "banana", "laranja"]
#frutas.remove ("banana")
#print(frutas) #["maçã". "laranja"]

#frutas.pop(0)
#print(frutas)  #["laranja"]


#TUPLAS
#tuplas são como listas, mas imutáveis. Elas são criadas com parênteses ().

#cores =("vermelho", "azul", "verde")
#numeros = (1, 2, 3, 4, 5)

#Acessando elementos

#print(cores[0]) #vermelho
#print(cores[-1]) #verde


#Tentando modificar uma tupla (ERRO!)

#cores[1] = "amarelho"  #isso gera um erro, pois tuplas são imutáveis


#convertendo entre lista e tupla
#Podemos converter uma tupla para uma lista e modificar os elementos.

#tupla = (1, 2, 3)
#lista = list(tupla)  #converte para lista
#lista.append(4)
#tupla = tuple(lista) #converte de volta para tupla
#print(tupla) #(1,2,3,4)

#Quando usar tuplas?

#- quando queremos garantir que os valores não sejam alterados
#- para armazenar dados fixos como coordenadas, meses do ano, dias da semana, etc.

meses = ("janeiro", "fevereiro", "março", "abril")
print(meses[2]) # março








         

      





