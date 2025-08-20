magnitud: float=float(input("Ingrese el numero de magnitud del terremoto: "))

if magnitud>0 and magnitud<3:
    print("Muy leve")
elif magnitud>=3 and magnitud<4:
    print("Leve")
elif magnitud>=4 and magnitud<5:
    print("Moderado")
elif magnitud>=5 and magnitud<6:
    print("Fuerte")
elif magnitud>=6 and magnitud<7:
    print("Muy fuerte")
elif magnitud>=7 and magnitud<=10:
    print("Extremo")
else:
    print("El valor ingresado no es valido")