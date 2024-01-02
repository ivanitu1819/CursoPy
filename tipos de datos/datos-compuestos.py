
#Creando una lista(se puede modificar)
lista = ["Ivan iturralde", "Soy Ivan", True,1.80]

#Creando una tupla (no se puede modificar)
tupla = ["Ivan iturralde", "Soy Ivan", True,1.80]

#Esto es valido
lista[3] = "Maquinola" 

#Esto no se va a ejecutar
#tupla[3] = "Maquinola"

#Creando un conjunto(set)
#No se puede llamar a los elementos po su indice,no almacena datos duplicados
conjunto = {"Ivan Iturralde","Soy Ivan",True,1.85}

#print(conjunto[3]) -> no puede acceder al elemento

#Creando un diccionario(dict)
diccionario = {
    'nombre' : "Ivan Iturralde",
    'canal' :  "Pirigunding",
    'esta_emocionado' : True,
    'altura' : 1.84,
    'dato_duplicado' :"Soy Ivan"
}


print(diccionario['canal'])