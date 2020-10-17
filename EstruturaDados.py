from console_logging.console import Console
console = Console()


class Pilha:
    
    def __init__(self):
        self.__pilha = []
        
    def push(self, value):
        console.log("PUSH " + str(value))
        self.__pilha.append(value)
        
    def pop(self):
        console.info("POP")
        return self.__pilha.pop()
        
    def show(self):
        console.success("Pilha: {}".format(self.__pilha))
