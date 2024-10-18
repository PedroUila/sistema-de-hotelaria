from __future__ import annotations
from abc import ABC, abstractmethod
from random import randint

class Subject(ABC):
    @abstractmethod
    def subscribe():
        pass
    @abstractmethod
    def unsubscribe():
        pass
    @abstractmethod
    def notify():
        pass

class Reserva(Subject):
    statusDisponiveis = ["concluido", "em andamento", "pendente"]
    observerList: list[Observer] = []
    def __init__(self, numQuarto):
        self.dataHoraReserva = None
        self.numDiasReserva = None
        self.senhaReserva = None
        self.statusReserva = ""
        self.numQuarto = numQuarto

    def subscribe(self, observer: Observer):
        self.observerList.append(observer)

    def unsubscribe(self, observer: Observer):
        self.observerList.remove(observer)

    def notify(self):
        for observer in self.observerList:
            observer.update(self)

    def trocarStatus(self):
        self.statusReserva = self.statusDisponiveis[randint(0, 2)]
        self.notify()



class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject):
        pass

class Hospede(Observer):

    def __init__(self) -> None:
        self.idHospede = idHospede
        self.nomeHospede = nomeHospede
        self.cpfHospede = cpfHospede
        self.emailHospede = emailHospede
        self.senhaHospede = senhaHospede

class Quarto(Observer):
    def __init__(self, numQuarto) -> None:
        self.idQuarto = None
        self.numQuarto = numQuarto
        self.andarQuarto = None
        self.disponivel = True
        self.statusQuarto = "nada"

    def __str__(self) -> str:
        return f"{self.numQuarto}"

    def update(self, subject: Subject):
        if subject.statusReserva == "concluido" and subject.numQuarto == self.numQuarto:
            self.disponivel = True
            print(f"QUARTO {self.numQuarto} ✅")
        elif subject.statusReserva == "em andamento" and subject.numQuarto == self.numQuarto:
            self.disponivel = False
            print(f"QUARTO {self.numQuarto} ❌")
        elif subject.statusReserva == "pendente" and subject.numQuarto == self.numQuarto:
            self.disponivel = False
            print(f"QUARTO {self.numQuarto} ❌")
        

r1 = Reserva(1)
r2 = Reserva(2)


quarto1 = Quarto(1)
quarto2 = Quarto(2)
quarto3 = Quarto(3)

Reserva.subscribe(quarto1)
Reserva.subscribe(quarto2)


r1.trocarStatus()
r2.trocarStatus()

