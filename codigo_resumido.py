from __future__ import annotations
from abc import ABC, abstractmethod

class Observador(ABC):
    @abstractmethod
    def update(self, publicador: Publicador):
        pass

class Publicador():
    def __init__(self) -> None:
        self.lista_observadores = []

    def sub(self, observador: Observador):
        self.lista_observadores.append(observador)

    def unsub(self, observador: Observador):
        self.lista_observadores.remove(observador)

    def notify(self):
        for observer in self.lista_observadores:
            observer.update(self)

class Reserva(Publicador):
    def __init__(self, id_reserva):
        super().__init__()
        self.id_reserva = id_reserva
        self.status_reserva = "pendente"

    def confirmar_reserva(self):
        self.status_reserva = "confirmado"
        self.notify()

    def cancelar_reserva(self):
        self.status_reserva = "cancelado"
        self.notify()

class Quarto(Observador):
    def __init__(self, numQuarto):
        self.numQuarto = numQuarto
    
    def update(self, publicador: Publicador):
        if publicador.status_reserva == "confirmado":
            print(f"O quarto {self.numQuarto} foi ocupado!")

class Hospede(Observador):
    def __init__(self, nomeHospede):
        self.nomeHospede = nomeHospede

    def update(self, publicador: Reserva):
        if publicador.status_reserva == "confirmado":
            print(f"{self.nomeHospede} a reserva foi realizada com sucesso!")



if __name__ == "__main__":
    hospede = Hospede("Thales")
    quarto = Quarto(57)

    reserva = Reserva(106)

    reserva.sub(quarto)
    reserva.sub(hospede)

    reserva.confirmar_reserva()
