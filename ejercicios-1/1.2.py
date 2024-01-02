frase = input("decime una frase y te calculo cuanto tardarias si tuvieras que decirla: ")

# CREAMOS UNA LISTA CON TODAS LAS PALABRAS DE LA FRASE
# (SE SEPARAN CADA VEZ QUE HAY UN ESPACIO EN BLANCO)
palabras_separadas = frase.split(" ")

# USAMOS LEN() PARA VER LA CANTIDAD DE ELEMENTOS QUE HAY EN LA LISTA
cantidad_de_palabras = len(palabras_separadas)

# EN CASO DE QUE TARDE MAS DE UN MINUTO EN DECIRLO, LE DECIMOS QUE PARE UN POCO
if cantidad_de_palabras > 30:
    print("Para flaco tampoco te pedi un testamento")

# CALCULAMOS CUANTO TARDARIA EN DECIR LAS PALABRAS Y SE LO DECIMOS
print(f'Dijiste  {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo')
print(f'Dalto lo diria en {cantidad_de_palabras*100 // 2 -1.3 / 100} segundos')
