def multiplos(num1, num2, num):
    if num1 < num2:
        cont = 0
        for i in range(num1, num2+1):
            if i % num == 0:
                cont = cont + 1
        print(cont)
    else:
        print("El primer numero debe ser menor al segundo numero")

