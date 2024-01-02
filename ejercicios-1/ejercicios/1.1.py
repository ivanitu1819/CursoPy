#PROMEDIO DE DURACION
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#DURACION DE CRUDOS
crudo_promedio = 5
crudo_dalto = 3.5


#DIFERENCIAS DE DURACION
diferencias_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencias_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
diferencias_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

#CALCULANDO EL PORCENTAJE DE TIEMPO VACIO REMOVIDO
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_promedio / 10

#MOSTRANDO LAS DIFERENCIAS DE DURACION(EJERCICIO A)
print("- - - - - - - - - - -")
print("El curso de dalto dura:")
print(f' - un {diferencias_con_min} % menos que el mas rapido')
print(f' - un {diferencias_con_max} % menos que el mas lento')
print(f' - un {diferencias_con_promedio} % menos que el promedio')
print("- - - - - - - - - - -")


#MOSTRANDO LA CANTIDAD DE ESPACIOS VACIOS QUE SE REMUEVEN (EJERCICIO B)
print(f'Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'Este curso elimino el {tiempo_vacio_dalto}% de tiempo vacio')
print("- - - - - - - - - - -")


#MOSTRANDO DIFERENCIAS SI LOS CURSOS DURARAN 10 HORAS
print(f'Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otros cursos')
print(f'Ver 10 horas de otros cursos equivale a ver {dalto_curso * 100 // otros_cursos_promedio / 10} horas de este cursos')
print("- - - - - - - - - - -")