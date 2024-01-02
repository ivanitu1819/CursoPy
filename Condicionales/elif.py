ingreso_mensual = 81000
gasto_mensual = 80000

# if anidados y else if(elif)

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Bien pa, estas bien")
    else:
        print("y pa, estas gastando una banda, que ver si te alcanza")

    
elif ingreso_mensual > 1000:
    print("Estas bien en latinoamerica")
    
elif ingreso_mensual > 500:
    print("Estas bien en argentina")
    
elif ingreso_mensual > 200:
    print("Estas bien en venezuela")    

else:
    print("Sos muy pobre")