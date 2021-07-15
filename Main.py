from Interrupciones_multiples import *

def main():
    print("Bienvenido al programa de simulacion de interruccion multiple")
    print("para comenzar introduzca el nombre del del dispositivo y seguido la prioridad (ejemp: 'Relog 3) y precione 0 si desea parar de ingresar IMPORTANTE: mientras menos sea el numero de la prioridad, mayor es su prioridad")
    nuevo_usuario = Interucciones_multiple()
    while True:
        Dispositivo_Prioridad = input("Introduzca el dispositivo seguido de su prioridad: ")
        if Dispositivo_Prioridad == "0":
            break
        Dispositivo_Prioridad = Dispositivo_Prioridad.split(" ")
        if  (nuevo_usuario.Agregar_Dispositvo(Dispositivo_Prioridad[0], Dispositivo_Prioridad[1])):
            print(("Se ha ingresado con exito el disositivo: {} con prioridad {}").format(Dispositivo_Prioridad[0],Dispositivo_Prioridad[1]))
        else:
            print("Se a obtenido un error con los datos introducido, porfavor introduce nuevamente")
    nuevo_usuario.proceso[0][2] = int(input("\nIntroduzca el tiempo que va a durar el programa sin interruccion"))
    print("A continuacion va a desglozar los procesos en el orden que ocurre, primero ingresando el segundo cuando inicia, el dispositvo y la Duracion (ejemplo: 3 computadora 5) en este ejemplo la computadora inica a los 3 seg y su duracion es de 5seg\nPrecione 0 si desea dejar de ingresar proceso")
    while True:
        proceso = input("\nIntroduzca el proceso: ")
        if proceso == "0":
            break
        proceso = proceso.split(" ")
        if  (nuevo_usuario.Agrergar_proceso(proceso[0], proceso[1],proceso[2])):
            print("Se ha ingresado con exito el proceso")
        else:
            print("Se a obtenido un error con los datos introducido, porfavor introduce nuevamente")
    tiempo_proceso = nuevo_usuario.simulacion_proceso()
    print("La simulacion a sido un exito\n")
    while True:
        print("\nMenu para analizar todo el proceso")
        menu_index = int(input("Para saber cuanto duro el programa precione:2\nPara hacer una busqueda de tiempo en el proceso precione:1\nPara salir precione:0\n"))
        if menu_index == 2:
            print(("El timpo total del prgrama fue:{}\n").format(tiempo_proceso))
        elif menu_index == 1:
            while True:
                tiempo = int(input("Introduzca en que segundo desea hacer la busqueda: "))
                nuevo_usuario.busqueda_proceso(tiempo)
                aux_menu_1 = int(input("\nDesea seguir haciendo busqueda? (para seguir precione:1, de lo contrario:0): "))
                if aux_menu_1 == 0:
                    break
        elif menu_index == 0:
            break
            
       
    
        



main()