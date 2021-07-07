class Interucciones_multiple():
    """Esta clase esta creada para hacer todas las operaciones necesarias para representar las interrucciones multiple"""
    def __init__(self,Duracion_Programa):
        self.Duracion_Programa = Duracion_Programa
        self.Dispositivo_Prioridad = {}
        self.proceso = []
        self.cola = []
        Programa
    def Agregar_Dispositvo(self,Dispositivo,Prioridad):
        """Agrega los dispositivon en conjunto con su prioridad y los coloca en el diccionario"""
        self.Dispositivo_Prioridad[Dispositivo] = Prioridad

    def Agrergar_proceso(self,Tiempo_inicial_Proceso,Dispositivo,Duracion):
        """Optiene los 3 datos: El tiempo en el que inicia, el dispositivo que corresponde y la duracion del proceso, y los coloca en una lista dentro de la Lista *Procesos*"""
        self.proceso.append([Tiempo_inicial_Proceso,Dispositivo,Duracion])   
        
    def Jerarquia(self,aux):
        """Esta funcion retorna verdadero si el dispositivo siguiente tiene una mayor prioridad, y false si tiene una menor prioridad"""
        if self.Dispositivo_Prioridad.get(self.proceso[aux][2])> self.Dispositivo_Prioridad.get(self.proceso[aux+1][2]):
            return True
        else:
            return False
            
    def Interruccion_proceso(self,tiempo):
        pass

    def Interruccion_programa(self,tiempo,aux):
        """Si se esta ejecutando el programa y lo interrumple un dispositivo esta funcion retorna verdadero, al tomar el tiempo en que comienza el dispositivo, si en ese momento ningun dispositivo arranca, este retorna falso"""
        try:
            if self.proceso[aux][0] == tiempo:
                return True
            else:
                return False
        except:False

    def Cola_espera(self,dispositivo_numero,tiempo_faltante):
        self.cola.append(dispositivo_numero,tiempo_faltante)
        
    def Desarrollo(self):
        tiempo = 0
        aux = 0
        tiempo_proceso = 0
        for i in range(self.Duracion_Programa):
            tiempo = tiempo + 1
            print("estoy dentro del programa")
            if self.Interruccion_programa(tiempo,aux):
                tiempo_empezandoPrograma = 0
                for j in range(self.proceso[aux][2]):
                    tiempo = tiempo + 1
                    try:
                        if (self.proceso[aux][2]+tiempo_empezandoPrograma)>self.proceso[aux+1][0]:
                            if self.Jerarquia(aux):
                                while tiempo < self.proceso[aux+1][0]:
                                    print(("Estoy en el ${}").format(self.proceso[aux][1]))
                                    tiempo_proceso = tiempo_proceso + 1
                                    tiempo = tiempo + 1
                                self.Cola_espera(aux,(proceso[aux][2]-tiempo_proceso))
                                aux = aux + 1
                    except: 
                            print("no hay con que verlo")
                    print(("Estoy en el {}").format(self.proceso[aux][1]))
                aux = aux + 1
                    
                            
           
# x = Interucciones_multiple()
# x.Programa(40)              
# x.Agregar_Dispositvo("computadora",10)
# x.Agregar_Dispositvo("impresora",5)
# x.Agregar_Dispositvo("relog",1)
# x.Agrergar_proceso(5,"computadora",3)
# x.Agrergar_proceso(10,"impresora",5)
# x.Agrergar_proceso(17,"relog",4)
# x.Desarrollo()
     
                    
                    



                





            
            


        



    
