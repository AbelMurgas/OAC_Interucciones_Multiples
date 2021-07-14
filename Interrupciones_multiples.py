class Interucciones_multiple():
    """Esta clase esta creada para hacer todas las operaciones necesarias para representar las interrucciones multiple"""
    def __init__(self):
        self.Dispositivo_Prioridad = {"programa":0,} #El programa siempre va a tener la menor prioridad
        self.proceso = []
        self.Clasificacion_procesos_list = []
    
    def Agregar_Dispositvo(self,Dispositivo,Prioridad):
        """Agrega los dispositivon en conjunto con su prioridad y los coloca en eu diccionario"""
        self.Dispositivo_Prioridad[Dispositivo] = Prioridad

    def Agrergar_proceso(self,Tiempo_inicial_Proceso,Dispositivo,Duracion):
        """Optiene los 3 datos: El tiempo en el que inicia, el dispositivo que corresponde y la duracion del proceso, y los coloca en una lista dentro de la Lista *Procesos*"""
        self.proceso.append([Tiempo_inicial_Proceso,Dispositivo,Duracion,False])   
        
    def Jerarquia_ASC(self,aux):
        """Esta funcion retorna verdadero si el dispositivo siguiente tiene una mayor prioridad, y false si tiene una menor prioridad"""
        if self.Dispositivo_Prioridad.get(self.proceso[aux][1]) > self.Dispositivo_Prioridad.get(self.proceso[aux+1][1]):
            return True
        else:
            return False

    def Jerarquia_DES(self,aux):
        """Esta funcion retorna verdadero si el dispositivo anterior tiene una mayor prioridad, y false si tiene una menor prioridad"""
        if self.Dispositivo_Prioridad.get(self.proceso[aux][1]) > self.Dispositivo_Prioridad.get(self.proceso[aux-1][1]):
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
        """dirije el auxiliar al punto en el proceso que debe ser desarrollado, dependiendo de tanto jerarquia(quien tiene mas prioridad) como si es el unico proceso pendiente, este retornara el auxialiar que dirige el proximo proxeso a ejecutarse"""

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
        time = 0 #El tiempo en todo el trayecto del proceso
        while (len(self.proceso))!= 0: #esta simulacion sera dada hasta que todos los procesos terminen
            aux = self.Punto_Proceso(aux,time)
            tiempo_proceso = self.proceso[aux][2]
            tiempo_inicial = time
            for i in range(self.proceso[aux][2]): #Comienzo del proceso
                tiempo_proceso = tiempo_proceso - 1
                time = time + 1
                if tiempo_proceso == 0: #Significa que el proceso termino, llegando su duracion a 0
                    self.Clasificacion_procesos(tiempo_inicial, self.proceso[aux][1], time, False)
                    self.proceso.pop(aux)
                    aux = aux - 1
                if self.Interruccion_proceso(time, aux): 
                    if self.Jerarquia_ASC(aux):
                        self.proceso[aux+1][3] = True
                    else:
                        if tiempo_proceso == 0:
                            break
                        self.Clasificacion_procesos(tiempo_inicial, self.proceso[aux][1], time, True)
                        self.proceso[aux][3] = True
                        self.proceso[aux][2] = tiempo_proceso
                        break
            aux = aux + 1
        return time

    def Clasificacion_procesos(self,tiempo_inicial,dispositivo,tiempo_final, interrumpido):
        """Recopila informacion de la simulacion del proceso, para obtener el tiempo inicial, el final, el dispositivo que esta acuando en ese rango de tiemo, y si esyte fue interrumpido o no"""
        self.Clasificacion_procesos_list.append([tiempo_inicial,tiempo_final,dispositivo,interrumpido])

    def Desglosado_tiempo(self):
        pass
                    
                            
           
x = Interucciones_multiple()

x.Agregar_Dispositvo("COM3",8)
x.Agregar_Dispositvo("Co-Proc Matematico",12)
x.Agregar_Dispositvo("Red",14)
x.Agregar_Dispositvo("Floppy-Diskette",4)

x.Agrergar_proceso(0, "programa", 10)
x.Agrergar_proceso(4,"COM3",8)
x.Agrergar_proceso(9,"Co-Proc Matematico",5)
x.Agrergar_proceso(12,"Floppy-Diskette",15)
x.Agrergar_proceso(25,"Red",12)
x.Agrergar_proceso(35,"COM3",3)
x.Agrergar_proceso(43,"Co-Proc Matematico",5)

x.Desarrollo()

                    






                





            
            


        



    
