from Interrupciones_multiples import *
import os
from colorama import *

def main():
    print("\033[4m"+"Bienvenido al programa de simulacion de interruccion multiple"+"\n\033[0;0m")
    print("para comenzar introduzca el nombre del dispositivo y seguido la prioridad (ejemp: 'Relog 3) y precione 0 si desea parar de ingresar."+"\n\033[4;31m"+"IMPORTANTE: mientras menos sea el numero de la prioridad, mayor es su prioridad"+"\033[0m")
    nuevo_usuario = Interucciones_multiple()
    while True:
        Dispositivo_Prioridad = input("Introduzca el dispositivo seguido de su prioridad: ")
        if Dispositivo_Prioridad == "0":
            break
        Dispositivo_Prioridad = Dispositivo_Prioridad.split(" ")
        if  (nuevo_usuario.Agregar_Dispositvo(Dispositivo_Prioridad[0], Dispositivo_Prioridad[1])):
            print(("\033[;32m"+"Se ha ingresado con exito el disositivo: {} con prioridad {}"+"\033[0m").format(Dispositivo_Prioridad[0],Dispositivo_Prioridad[1]))
        else:
            print("\n\033[4;31m"+"Se a obtenido un error con los datos introducido, porfavor introduce nuevamente"+"\033[0m")
    nuevo_usuario.proceso[0][2] = int(input("\nIntroduzca el tiempo que va a durar el programa sin interruccion: "))
    print("A continuacion va a desglozar los procesos en el orden que ocurre, primero ingresando el segundo cuando inicia, el dispositvo y la Duracion (ejemplo: 3 computadora 5) en este ejemplo la computadora inica a los 3 seg y su duracion es de 5seg\nPrecione 0 si desea dejar de ingresar proceso")
    while True:
        proceso = input("\nIntroduzca el proceso: ")
        if proceso == "0":
            break
        proceso = proceso.split(" ")
        if  (nuevo_usuario.Agrergar_proceso(proceso[0], proceso[1],proceso[2])):
            print("\033[3;32m"+"Se ha ingresado con exito el proceso"+"\033[0m")
        else:
            print("\n\033[4;31m"+"Se a obtenido un error con los datos introducido, porfavor introduce nuevamente"+"\n\033[0m")
    tiempo_proceso = nuevo_usuario.simulacion_proceso()
    print("\033[3;32m"+"\n-----------La simulacion a sido un exito------------------\n"+"\033[0m")
    print("\033[;;44m")
    while True:
        menu_index = int(input(
        """

                _Menu para analizar todo el proceso_
        ____________________________________________________
        |0.Para salir                                       |
        |1.Para hacer una busqueda de tiempo en el proceso  |
        |2.Para saber cuanto duro el programa               |
        |___________________________________________________|



"""))
        os.system('cls')
        if menu_index == 2:
            print(("\033[4m"+"El tiempo total del programa fue de: {}seg\n").format(nuevo_usuario.time
            )+"\033[;;44m")
        elif menu_index == 1:
            while True:
                tiempo = int(input("Introduzca en que segundo desea hacer la busqueda: "))
                nuevo_usuario.busqueda_proceso(tiempo)
                aux_menu_1 = int(input("\nDesea seguir haciendo busqueda? (para seguir precione:1, de lo contrario:0): "))
                if aux_menu_1 == 0:
                    break
        elif menu_index == 0:
            break
    print("\033[0;0m")
main()
