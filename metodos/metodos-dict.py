# NOS DEVUELVE UN OBJETO DICT_ITEM
diccionario = {
    "nombre" : 'ivan',
    "apellido" : 'iturralde',
    "subs" : '0'
}


claves = diccionario.keys()


#OBTENIENDO UN ELEMENTO CON GET() SI NO ENCUENTRA NADA EL PROGRAMA CONTINUA
valor_de_subs = diccionario.get("subs")

# ELIMINANDO TODO DEL DICCIONARIO
diccionario.clear()

# ELIMINANDO UN ELEMENTO DEL DICCIONARIO
diccionario.pop("apellido","nombre")

# OBTENIENDO UN ELEMENTO DICT_ITEMS ITERABLE
diccionario_iterable = diccionario.items()

print(claves)