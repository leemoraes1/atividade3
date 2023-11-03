class Monitor:
    def __init__ (self, marca, polegada, resolucao, hertz):
        self.marca = marca
        self.polegada = polegada
        self.resolucao = resolucao
        self.hertz = hertz


    def __str__ (self):
        return f"Monitor {self.marca} com {self.polegada} na resolução {self.resolucao} com {self.hertz}hz"

class Computador:
    def __init__ (self, processador, ram, memInt, placaVid):
        self.processador = processador
        self.ram = ram
        self.memInt = memInt
        self.placaVid = placaVid
        self.monitor = None

    def conectaMonitor (self, monitor):
        self.monitor = monitor

    def __str__ (self):
        if self.monitor:
            return f"Computador na configuração {self.processador}, {self.ram}, {self.memInt} e {self.placaVid} conectado no {self.monitor}"
        else:
            return f"Computador com a configuração {self.processador}, {self.ram}, {self.memInt} e {self.placaVid} não está conectado a nenhum monitor"
        
monitor1 = Monitor("LG", "18 polegadas", "2560x1440", 144)
computador1 = Computador("I5", "8Gb", "500Gb", "Gtx980")

print(computador1)
print(monitor1)
computador1.conectaMonitor(monitor1)
print(computador1)