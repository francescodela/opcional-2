print ('REGISTRO')

#def validar_usuario ():



while (True):
    try:
        nombre  = str(input("Ingresa el nombre  "))
    except TypeError:
        print("solo se pueden letras.")
    break 
while (True):


    try:
        edad = int(input("Ingresa tu edad: "))
        if edad < 0:
            print("La edad no puede ser negativa.")
        elif edad > 120:
            print("Eres mayor  de edad.")
        
    except ValueError:
        print("solo se pueden  numeros enteros.")
        print("ingresa un numero de entre 0 a 120.")
    break         
while (True):
    try:
        nombre  = (input("Ingresa el Email  "))
    except TypeError:
        print("solo se pueden letras.")

    break 
    
                
            
        


'''
• NombreInvalidoError: si el nombre contiene números o símbolos.
• EdadInvalidaError: si la edad no es un número entero entre 0 y 120.
• CorreoInvalidoError: si el correo no contiene "@" o tiene espacios.
'''