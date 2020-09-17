def rangos(num1, num2, num):
    cont = 0
    if num1 < num2:
        for i in range(num1, num2):
            if i % num == 0:
                cont += cont
                print(cont)
    else:
        print("el primer numero debe ser menor al segundo numero")
