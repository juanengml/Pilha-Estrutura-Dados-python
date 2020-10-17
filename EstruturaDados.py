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


