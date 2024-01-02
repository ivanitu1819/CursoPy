# CREANDO DICCIONARIOS CON DICT() & DICCIONARIOS VACIOS
diccionario = dict(nombre = "Ivan" ,apellido = "Iturralde")

# LAS LISTAS NO PUEDE SER CLAVES Y USAMOS FROZENSET PARA METER CONJUNTOS
diccionario = {frozenset(["Ivan","Crack" ]):"Jaja"}

# CREANDO DICCIONARIOS CON FROMKEYS() VALOR POR DEFECTO: NONE
diccionario = dict.fromkeys(["nombre", "apellido"])

# CREANDO DICCIONARIOS CON FROMKEYS() CAMBIANDO EL VALOR POR DEFECTO A "NO SE"
diccionario = dict.fromkeys(["nombre", "apellido"],"NO SE")


print(diccionario)
