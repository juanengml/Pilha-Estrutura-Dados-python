from console_logging.console import Console
console = Console()


class Pilha:
    
    def __init__(self):
        console.log("START PILHAS ")
        self.__pilha = []
        
    def push(self, value):
        console.log("PUSH " + str(value))
        self.__pilha.append(value)
        
    def pop(self):
        console.info("POP")
        return self.__pilha.pop()
        
    def show(self):
        console.success("Pilha: {}".format(self.__pilha))


class Filas:
    def __init__(self):
        console.log("STARTING QUEUE")
        self.__fila = []

    def insere(self, value):
        console.log("INSERE NA Fila " + str(value))
        self.__fila.append(value)

    def remove(self):
        console.log("POP DATA")
        return self.__fila.pop(0)

    def show(self):
        console.success(f'Queue: {self.__fila}')

class Node:
    def __init__(self, value, arquivo ,proximo=None):
        self.__value = value
        self.arquivo = arquivo
        self.proximo = proximo

    @property
    def value(self):
        return self.__value


class ListaEncadeadaSimples:
    def __init__(self):
        self.__main_node = None

    def append(self, value,arquivo):
        if self.__main_node is None:
            self.__main_node = Node(value,arquivo)
            return

        proximo_node = self.__main_node
        while proximo_node.proximo is not None:
            proximo_node = proximo_node.proximo
        proximo_node.proximo = Node(value,arquivo)

    def remove(self, value):
        if self.__main_node is None:
            return

        left_node = None
        proximo_node = self.__main_node

        if proximo_node.value == value:
            self.__main_node = proximo_node.proximo

        while True:
            left_node = proximo_node
            proximo_node = proximo_node.proximo

            if proximo_node is None:
                break

            if proximo_node.value == value:
                left_node.proximo = proximo_node.proximo

    def show(self):
        values = []
        proximo_node = self.__main_node
        while proximo_node is not None:
            data = {
              "arquivo.txt":  proximo_node.arquivo,
              "frequencia": proximo_node.value
            }
            values.append(data)
            proximo_node = proximo_node.proximo
        list_ordenada = sorted(values, key=lambda k: k['frequencia']) 
            
        print("list_ordenada: {}".format(list_ordenada))

