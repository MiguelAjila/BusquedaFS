#FIFO First im first out (Primero en entrar, primero en salir)
#Importamos la libreria fifo "queue"
from queue import Queue
#Se debe crear funciones contienen metodos y variables
class Grafo:
    """
    Se crea una clase denominada Grafo, esta permite crear diferentes metodos y variables.
    Se implemento el contructor __init__
    con ayuda de un "def" se crea un metodo, utilizando la variable "num_nodos".
    El uso del comando self vincula los datos y se los agrega aun arreglo o tambien denominado lista.
    --------------------------------------------------------------------------------------------------------------
    El siguiente codigo tiene la funcion de un diccionario

    "def __init__(self, num_nodos, direccion=True):
        self.m_num_nodos = num_nodos
        self.m_nodos = range(self.m_num_nodos)"

    """
    # Constructor
    # El uso de Self permite el funcionamiento automatico
    def __init__(self, num_nodos, direccion=True):
        """"
        El siguiente metodo tiene la funcion de un diccionario, con los atributos, self
        permite el ordenamientos, mientras range los almacena en una lista.
        Utilizando las sentencia
        "self.m_direccion = direccion"
        Permite colocar al director unidireccional a la lista adyacente.
        Para el almacenamiento de los datos adyacentes se utiliza las sentencias
        "self.m_list_adj = {nodo: set() for nodo in self.m_nodos}"

        """

        self.m_num_nodos = num_nodos
        self.m_nodos = range(self.m_num_nodos)

         # Director unidireccional
        self.m_direccion = direccion
		
        # Representación gráfica - Lista de adyacencia
        self.m_list_adj = {nodo: set() for nodo in self.m_nodos}      
	
    # Agregamos en los borde al gráfico
    # Colocamos variables de nodo y peso
    def agg_nodo(self, nodo1, nodo2, peso=1):
        self.m_list_adj[nodo1].add((nodo2, peso))
