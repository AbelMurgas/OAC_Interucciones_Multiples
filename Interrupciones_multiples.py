class Interucciones_multiple():
    """Esta clase esta creada para hacer todas las operaciones necesarias para representar las interrucciones multiple"""
    def __init__(self):
        self.Dispositivo_Prioridad = {"programa":1000,} #El programa siempre va a tener la menor prioridad
        self.proceso = [[0,"programa",10,False]]
        self.Clasificacion_procesos_list = []
        self.time = 0
        self.cola = []
    def Agregar_Dispositvo(self,Dispositivo,Prioridad): 
        """Agrega los dispositivon en conjunto con su prioridad y los coloca en eu diccionario"""
        Dispositivo = Dispositivo.lower()
        try:
            self.Dispositivo_Prioridad[Dispositivo] = int(Prioridad)
            return True
        except:
            return False

    def cola_pendiente(self,nombre,tiempo_faltante):
        self.cola.append([nombre,tiempo_faltante])
        
    def Dispositivo_igual(self,dispositivo):
        for i in self.Dispositivo_Prioridad:
            if i == dispositivo:
                return True
        return False

    def Agrergar_proceso(self,Tiempo_inicial_Proceso,Dispositivo,Duracion):
        """Optiene los 3 datos: El tiempo en el que inicia, el dispositivo que corresponde y la duracion del proceso, y los coloca en una lista dentro de la Lista *Procesos*"""
        Dispositivo = Dispositivo.lower()
        try:
            self.proceso.append([int(Tiempo_inicial_Proceso),Dispositivo,int(Duracion),False]) 
            return True
        except:
            return False  
        
    def Jerarquia_ASC(self,aux):
        """Esta funcion retorna verdadero si el dispositivo siguiente tiene una mayor prioridad, y false si tiene una menor prioridad"""
        if self.Dispositivo_Prioridad.get(self.proceso[aux][1]) < self.Dispositivo_Prioridad.get(self.proceso[aux+1][1]):
            return True
        else:
            return False

    def Jerarquia_DES(self,aux):
        """Esta funcion retorna verdadero si el dispositivo anterior tiene una mayor prioridad, y false si tiene una menor prioridad"""
        if self.Dispositivo_Prioridad.get(self.proceso[aux][1]) < self.Dispositivo_Prioridad.get(self.proceso[aux-1][1]):
            return True
        else:
            return False
            
    def Interruccion_proceso(self,tiempo,aux):
        """Si se esta ejecutando un proceso lo interrumpen esta funcion retorna verdadero, al tomar el tiempo en que comienza el dispositivo, si en ese momento ningun dispositivo arranca, este retorna falso"""
        try:
            if self.proceso[aux+1][0] == tiempo:
                return True
            else:
                return False
        except:False

    def Punto_Proceso(self,aux,time):
        """dirije el auxiliar al punto en el proceso que debe ser desarrollado, dependiendo de tanto jerarquia(quien tiene mas prioridad) como si es el unico proceso pendiente, este retornara el auxialiar que dirige el proximo proceso a ejecutarse"""

        if (len(self.proceso)) <= aux: #Si el auxiliar llega a medir mas que la longitud
            aux = len(self.proceso)-1 #Se coloca el auxiliar al punto maximo de la lista
        try:
            if self.proceso[aux-1][3] == True: #Si el anterior esta esperado
                if aux > 2: #Verifica si el aux es mayor a 2, ya que este caso signigica que hay 2 o mas esperando 
                    for n in (aux-1): #itera cada uno de ellos,Buca el mayor en jerarquia para cambiar el auxiliar
                        if not self.Jerarquia_DES(aux): 
                            aux = aux - 1
                    return aux
                elif self.proceso[aux][0] <= time: #si el actual esta iniciando o esta esperando
                    if not self.Jerarquia_DES(aux): 
                        return (aux-1)
                    return aux
                else:
                    return (aux-1)
            else:
                return aux
        except:
                if len(self.proceso) == 1:
                    return (aux-1)
                else:
                    return aux

    def simulacion_proceso(self):
        """Simula el proceso ya habiendo obtenido los dispositivos y los datos de cada uno de los proceso"""
        aux = 0 #El auxiliar, apunta a una dirreccion en la lista
        while (len(self.proceso))!= 0: #esta simulacion sera dada hasta que todos los procesos terminen
            aux = self.Punto_Proceso(aux,self.time)
            tiempo_proceso = self.proceso[aux][2]
            tiempo_inicial = self.time
            for i in range(self.proceso[aux][2]): #Comienzo del proceso
                tiempo_proceso = tiempo_proceso - 1
                self.time = self.time + 1
                if tiempo_proceso == 0: #Significa que el proceso termino, llegando su duracion a 0
                    self.Clasificacion_procesos(tiempo_inicial, self.proceso[aux][1],self.time, False, False,0)
                    self.proceso.pop(aux)
                    aux = aux - 1
                if self.Interruccion_proceso(self.time, aux): 
                    if self.Jerarquia_ASC(aux):
                        self.cola_pendiente(self.proceso[aux+1][1],self.proceso[aux+1][2])
                        self.proceso[aux+1][3] = True   
                    else:
                        if tiempo_proceso == 0:
                            break
                        self.Clasificacion_procesos(tiempo_inicial, self.proceso[aux][1],self.time, True, self.proceso[aux+1][1],tiempo_proceso)
                        self.cola_pendiente(self.proceso[aux][1],tiempo_proceso)
                        self.proceso[aux][3] = True
                        self.proceso[aux][2] = tiempo_proceso
                        break
            aux = aux + 1

    def Clasificacion_procesos(self,tiempo_inicial,dispositivo,tiempo_final, interrumpido, Dispositivo_interrumpio,Tiempo_Termina):
        """Recopila informacion de la simulacion del proceso, para obtener el tiempo inicial, el final, el dispositivo que esta acuando en ese rango de tiemo, y si esyte fue interrumpido o no"""
        mensaje_interrupcion = "No fue interrumpida"
        if interrumpido:
            mensaje_interrupcion = ("Fue interrumpida por el/la {}").format(Dispositivo_interrumpio)

        self.Clasificacion_procesos_list.append([tiempo_inicial,tiempo_final,dispositivo,mensaje_interrupcion, Tiempo_Termina])

    def busqueda_proceso_tiempo(self,tiempo): 
        """Hace busqueda de un proceso mediante el tiempo, retornando el dispositivo que estuvo en ese tiempo, si fue interrumpido, y su rango de tiempo en el proceso"""
        for i in self.Clasificacion_procesos_list:
            if i[0] <= tiempo and tiempo <= i[1]:
                print(("En el segudo {} se estaba ejecuntado el/la {}\nSu intervalo fue desde el segundo {} al segundo {}\n{}\ntiempo para que finalizara {}seg").format(tiempo,i[2],i[0],i[1],i[3],i[4]))
                break
    
    def busqueda_proceso_nombre(self,nombre):
        """Hace una busqueda de los procesos en el que estuvo un dispositivo"""
        interrupcion_total = 0
        for i in self.Clasificacion_procesos_list:
            if i[2] == nombre:
                print("\033[34m")
                print("____________________________________________________________________________")
                print(("Estuvo en el rango de {}seg a {}seg\n{}\ntiempo para que finalizara:{}seg").format(i[0],i[1],i[3],i[4]))
                if not i[3] == "No fue interrumpida":
                    interrupcion_total = interrupcion_total + 1
                print("\033[0m")
        if interrupcion_total == 0:
            print(("\nEl/La {} Nunca fue interrumpido").format(nombre,interrupcion_total))   
        elif interrupcion_total == 1:
            print(("\nEl/La {} fue interrumpido 1 sola vez").format(nombre,interrupcion_total))
        else:
            print(("\nEl/La {} fue interrumpida:{} veces").format(nombre,interrupcion_total))            

    def tabla_interrupcion(self):
        z = "-"
        print(" _______________________________________")
        print(("|{:^15}|{:^5}|{:^5}|{:^5}|{:^5}|").format("Dispositivo","Tp1","Tp2","Tp3","Tp4"))
        print(" _______________________________________")
        for key in self.Dispositivo_Prioridad:
            conteiner = []
            for i in self.cola:
                if key == i[0]:
                        conteiner.append(i[1])
            if len(conteiner) < 4:
                faltante = 4 - len(conteiner)
                for j in range(faltante):
                    conteiner.append(z)
            print(("""|{:^15}|{:^5}|{:^5}|{:^5}|{:^5}|""").format(key,conteiner[0],conteiner[1],conteiner[2],conteiner[3]))
            print(" _______________________________________")


    

                    
                            
           
                






                





            
            


        



    
