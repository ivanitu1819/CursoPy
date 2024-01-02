cadena1 = "Soy ivan"
cadena2 = "Bienvenido maquinola"


# LO CONVIERTE A MAYUSCULA
mayuscula = cadena1.upper() 

# LO CONVIERTE A minuscula
minuscula = cadena1.lower() 

# CONVIERTE PRIMERA LETRA A MAYUSCULA
primer_letra = cadena1.capitalize()


# BUSCAMOS UNA CADENA EN OTRA CADENA
# SI NO HAY COINCIDENCIA DEVUELVE -1
busqueda_find = cadena1.find("HOla") 


# BUSCAMOS UNA CADENA EN OTRA CADENA
# SI NO HAY COINCIDENCIA NOS DEVUELVE UNA EXCEPCION
busqueda_index = cadena1.index("a") 


# SI ES NUMERICO, DEVOLVEMOS TRUE, SINO DEVOLVEMOS FALSE
es_numerico = cadena1.isnumeric()


# SI ES ALFANUMERICO, DEVOLVEMOS TRUE, SINO DEVOLVEMOS FALSE
es_alfatanumerico = cadena1.isalpha()

# CONTAMOS LAS COINCIDENCIAS DE UNA CADENA, DENTRO DE OTRA CADENA
# DEVUELVE LA CANTIDAD DE VECES QUE COINCIDA
contar_coincidencias = cadena1.count("a")

# CONTAMOS CUANTOS CARACTERES TIENE UNA CADENA
contar_cantidad_de_caracteres = len(cadena1)

# VERIFICAMOS SI UNA CADENA EMPIEZA CON OTRA CADENA DADA, 
# SI ES ASI DEVUELVE TRUE
empieza_con = cadena1.startswith("H")


# VERIFICAMOS SI UNA CADENA TERMINA CON OTRA CADENA DADA, 
# SI ES ASI DEVUELVE TRUE
termina_con = cadena1.endswith("an")


# SI EL VALOR 1, SE ENCUENTRA EN LA CADENA ORIGINAL, REMPLAZA EL VALOR 1
# DE LA MISMA POR EL VALOR 2
cadena_nueva = cadena1.replace("ivan","advantek")


# SEPARAR CADENAS CON LA CADENA QUE LE PASEMOS
cadena_separada = cadena1.split(",")





print(cadena_separada)