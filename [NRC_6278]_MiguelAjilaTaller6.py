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
	
	"""
        El metodo denominado "agg_nodo", aqui verifica el peso y agregara
        un nodo en el borde del grafico, a su vez se utilizan las condicionales.
        Donde se comprueba si los nodos contienen algun valor o vacio.
        En caso de contener valor agregara a la lista adyacente.
        """  
        #Utilizamos una condicional
        #donde colocamos el director unidireccional para enlistar los adyacentes
        if not self.m_direccion:
            self.m_list_adj[nodo2].add((nodo1, peso))
    
    # Creamos una funcion donde permitira imprimir la secuencia de nodos
    def print_list_adj(self):
        """
        Se implementa el metodo de imprimir la lista de adyacencia. 
        """
        
        for key in self.m_list_adj.keys():
            # Con la condicional for, imprimeros cada segmento de la lista de adyacencia
            print("nodo", key, ": ", self.m_list_adj[key])


    # Función que pemrite BFS ordenar los nodos
    # Estos son atravesados por los vertices
    def bfs_vertice(self, nodo_inicio):
        # Declaramos los siguientes metodos 
        # Estas evitaran los bucles
        visita = set()
        queue = Queue()
	# Comenzamos a ordena los nodos, declarando un nodo_inicio
        # La cola se comienza a en listar los nodos.
        queue.put(nodo_inicio)
        visita.add(nodo_inicio)

        while not queue.empty():
            # Desencolar un vértice para encolarlo e imprimirlo
            #Mientras no este vacia no realizara la busqueda
            nodo_actual = queue.get()
            print(nodo_actual, end = " ")
            """
            Verifica el nodo esta bien para dar acceso a la siguiente ruta
            Visita los adyacentes de las vertices donde si no esta visitado los coloca en la cola.
            """

            for (sig_nodo, peso) in self.m_list_adj[nodo_actual]:
                if sig_nodo not in visita:
                    queue.put(sig_nodo)
                    visita.add(sig_nodo)

if __name__ == "__main__":
    #### EJEMPLO #####

    # Instanciamos la clase de grafico donde el grafo es unidireccional
    # esta contiene 5 nodos
    g0 = Grafo(5, direccion=False)
    print(" Caso de Prueba 1")
    # Agregue bordes al gráfico con peso predeterminado = 1
    g0.agg_nodo(0, 1)
    g0.agg_nodo(0, 2)
    g0.agg_nodo(1, 2)
    g0.agg_nodo(1, 4)
    g0.agg_nodo(2, 3)
    
    # Utilizamos la funcion del grafico para agregar datos en el formulario
    # Imprimiendo la lista de adyacencia de forma ordenada
    g0.print_list_adj()

    print ("A continuación se muestra el recorrido primero en amplitud"
                    " (comenzando desde el vértice 0)")
    g0.bfs_vertice(0)
    print()
#--------------------------------------------------------------------------------------------------------------------

    g1 = Grafo(5, direccion=False)
    print(" Caso de Prueba 2")
    g1.agg_nodo(0, 1)
    g1.agg_nodo(0, 2)
    g1.agg_nodo(1, 3)
    g1.agg_nodo(1, 4)
    g1.agg_nodo(2, 3)
    g1.agg_nodo(2, 4)

    g1.print_list_adj() #Se imprime la lista de adyacencia
 
    print("A continuación se muestra el recorrido primero en anchura a partir del vértice 0)")
    #Imprime toda la lista de colas
    g1.bfs_vertice(0)
    print()

#--------------------------------------------------------------------------------------------------------------------

    g2 = Grafo(5, direccion=False)
    print(" Caso de Prueba 3")
    g2.agg_nodo(1, 2)
    g2.agg_nodo(0, 4)
    g2.agg_nodo(0, 3)
    g2.agg_nodo(1, 2)
    g2.agg_nodo(0, 4)
    g2.agg_nodo(0, 3)

    g2.print_list_adj() #Se imprime la lista de adyacencia
 
    print("A continuación se muestra el recorrido primero en anchura a partir del vértice 0)")
    #Imprime toda la lista de colas
    g2.bfs_vertice(0)
    print()

#--------------------------------------------------------------------------------------------------------------------

    g3 = Grafo(5, direccion=False)
    print(" Caso de Prueba 4")
    g3.agg_nodo(0, 2)
    g3.agg_nodo(0, 1)
    g3.agg_nodo(2, 4)
    g3.agg_nodo(1, 0)
    g3.agg_nodo(3, 2)
    g3.agg_nodo(3, 4)

    g3.print_list_adj() #Se imprime la lista de adyacencia
 
    print("A continuación se muestra el recorrido primero en anchura a partir del vértice 0)")
    #Imprime toda la lista de colas
    g3.bfs_vertice(0)
    print()

#--------------------------------------------------------------------------------------------------------------------

    g4 = Grafo(5, direccion=False)
    print(" Caso de Prueba 5")
    g4.agg_nodo(0, 1)
    g4.agg_nodo(0, 4)
    g4.agg_nodo(2, 3)
    g4.agg_nodo(1, 2)
    g4.agg_nodo(1, 4)
    g4.agg_nodo(1, 3)

    g4.print_list_adj() #Se imprime la lista de adyacencia

    g4.print_list_adj() #Se imprime la lista de adyacencia

    print("A continuación se muestra el recorrido primero en anchura a partir del vértice 0)")
    #Imprime toda la lista de colas
    g4.bfs_vertice(0)
    print()
