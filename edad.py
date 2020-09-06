def edad_futura(edadActual, añoActual):
    if edadActual > 0:
        if añoActual > 0:
            años = 2070 - añoActual
            nuevaEdad = edadActual+ años
            return nuevaEdad
        else:
            print("El año ingresado es erroneo ya que este es negativo")
    else:
        print("La edad ingresada es erronea ya que esta es negativa")
