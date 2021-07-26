from Interrupciones_multiples import *
import os
from colorama import *

def main():
    c = 0
    while c == 0:
        print("\033[4m"+"Bienvenido al programa de simulacion de interruccion multiple"+"\n\033[0;0m")
        print("para comenzar introduzca el nombre del dispositivo y seguido la prioridad"+"\033[36m"+" (ejemp: 'Relog 3) "+"\033[0m"+"y precione 0 si desea parar de ingresar."+"\n\033[4;31m"+"IMPORTANTE: mientras menos sea el numero de la prioridad, mayor es su prioridad"+"\033[0m")
        nuevo_usuario = Interucciones_multiple()
        while True:
            Dispositivo_Prioridad = input("Introduzca el dispositivo seguido de su prioridad: ")
            if Dispositivo_Prioridad == "0" or Dispositivo_Prioridad == "":
                break
            Dispositivo_Prioridad = Dispositivo_Prioridad.split(" ")
            Dispositivo_Prioridad[0] = Dispositivo_Prioridad[0].lower()
            if nuevo_usuario.Dispositivo_igual(Dispositivo_Prioridad[0]):
                print("\033[4;31m"+"Error a ingresado el mismo dispositivo"+"\033[0m")
            else:
                if  (nuevo_usuario.Agregar_Dispositvo(Dispositivo_Prioridad[0], Dispositivo_Prioridad[1])):
                    print(("\033[;32m"+"Se ha ingresado con exito el disositivo: {} con prioridad {}"+"\033[0m").format(Dispositivo_Prioridad[0],Dispositivo_Prioridad[1]))
                else:
                    print("\n\033[4;31m"+"Se a obtenido un error con los datos introducido, porfavor introduce nuevamente"+"\033[0m")
        while True:
            try:
                tiempo_programa = int(input("\nIntroduzca el tiempo que va a durar el programa sin interruccion: "))
                break 
            except:
                print("\033[4;31m"+"ERROR: Debe ser un tiempo valido"+"\033[0m") 
                print("Intentelo nuevamente")
        nuevo_usuario.proceso[0][2] = tiempo_programa
        print(("\033[;32m"+"Se agrego con exito el tiempo de duracion del programa:{}"+"\033[0m").format(tiempo_programa))
        print("\nA continuacion va a desglozar los procesos en el orden que ocurre, primero ingresando el segundo cuando inicia, el dispositvo y la Duracion\n"+"\033[36m"+"(ejemplo: 3 computadora 5) en este ejemplo la computadora inica a los 3 seg y su duracion es de 5seg"+"\033[0m"+"\nPrecione 0 si desea dejar de ingresar proceso")
        while True:
            proceso = input("\nIntroduzca el proceso: ")
            if proceso == "0" or proceso == "":
                break
            proceso = proceso.split(" ")
            proceso[1] = proceso[1].lower()
            if nuevo_usuario.Dispositivo_igual(proceso[1]):
                if  (nuevo_usuario.Agrergar_proceso(proceso[0], proceso[1],proceso[2])):
                    print("\033[3;32m"+"Se ha ingresado con exito el proceso"+"\033[0m")
                else:
                    print("\n\033[4;31m"+"Se a obtenido un error con los datos introducido, porfavor introduce nuevamente"+"\n\033[0m")
            else:
                print("\n\033[4;31m"+"Error el dispositivo que ha ingresado en el proceso no se encuentra en la base de datos"+"\n\033[0m")
                print("Los dispositivos en la base de datos son: ")
                for i in nuevo_usuario.Dispositivo_Prioridad:
                    if not i == "programa":
                        print("\033[34m"+i+"\033[0m")
        tiempo_proceso = nuevo_usuario.simulacion_proceso()
        print("\033[3;32m"+"\n-----------La simulacion a sido un exito------------------\n"+"\033[0m")
        
        while True:
            menu_index = int(input(
            """

                    _Menu para analizar todo el proceso_
            ____________________________________________________________
            |0.Para salir                                               |
            |1.Para hacer una busqueda de tiempo en el proceso          |
            |2.Para saber cuanto duro el programa                       |
            |3.Para hacer busqueda de procesos mediante el Dispositivo  |
            |4.Ver cola de procesos pendientes                          |
            |___________________________________________________________|



"""))
            os.system('cls')
            if menu_index == 4:
                nuevo_usuario.tabla_interrupcion()
            elif menu_index == 3:
                nombre = input("Ingrese el nombre del disposito: ")
                nuevo_usuario.busqueda_proceso_nombre(nombre)
            elif menu_index == 2:
                print(("El tiempo total del programa fue de: {}seg\n").format(nuevo_usuario.time
                ))
            elif menu_index == 1:
                while True:
                    tiempo = int(input("Introduzca en que segundo desea hacer la busqueda: "))
                    nuevo_usuario.busqueda_proceso_tiempo(tiempo)
                    aux_menu_1 = int(input("\nDesea seguir haciendo busqueda? (para seguir precione:1, de lo contrario:0): "))
                    if aux_menu_1 == 0:
                        break
            elif menu_index == 0:
                print("\033[3;32m"+"\n----------------Simulacion terminada----------------\n"+"\033[0m")
                c = int(input(("Desea hacer otra simulacion? (Si:preciones '0', No: precione '1') \n")))
                break
            else:
                print("Ingrese una opcion correcta")

main()
