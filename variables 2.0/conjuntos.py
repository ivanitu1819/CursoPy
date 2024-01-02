# CREANDO UN CONJUNTO CON SET()

conjunto = set(["Dato1", "Dato 2"])

# METIENDO UN CONJUNTO DENTRO DE UN CONJUNTO
conjunto1 = frozenset(["dato1", "dato2"])
conjunto2 = {conjunto1,"dato 3"}
print(conjunto2)

# TEORIA DE CONJUNTOS

conjunto1 = {1.3,5,7}
conjunto2 = {1,3,7}

# VERIFICANDO SI ES UN SUBCONJUNTO SUBSET O <=
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1
print(resultado)

# VERIFICANDO SI ES UN SUPERCONJUNTO SUBSET O =>
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1
print(resultado)

# VERIFICAR SI HAY ALGUN NUMERO EN COMUN
resultado = conjunto2.isdisjoint(conjunto1)