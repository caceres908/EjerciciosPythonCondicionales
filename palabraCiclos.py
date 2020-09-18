def palindroma(palabra):
    inver = ""
    for i in reversed(range(0, len(palabra))):
        inver += palabra[i]
    if palabra == inver:
        pal = True
    else:
        pal = False
    if pal:
        print("Es palindroma")
    else:
        print("No es palindroma")
    return pal
