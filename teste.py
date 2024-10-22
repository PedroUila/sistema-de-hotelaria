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
    def __init__(self, id_reserva: int):
        super().__init__()
        self.id_reserva = id_reserva
        self.reserva_realizada = False

    def realizar_reserva(self, quarto: Quarto):
        if quarto.disponivel:
            self.reserva_realizada = True
        self.notify()
            
class Quarto(Observador):
    def __init__(self, numQuarto):
        self.numQuarto = numQuarto
        self.disponivel = True
    
    def update(self, reserva: Reserva):
        if reserva.reserva_realizada:
            self.disponivel = False
            alerta = f"A reserva do quarto {self.numQuarto} foi realizada com sucesso!"
        else: 
            alerta = f"O quarto {self.numQuarto} já está ocupado, escolha outro!"
        print(alerta)
            
class Hospede(Observador):
    def __init__(self, nomeHospede):
        self.nomeHospede = nomeHospede

    def update(self, reserva: Reserva):
        if reserva.reserva_realizada:
            alerta = f"{self.nomeHospede}, a reserva foi realizada com sucesso!"
        else:
            alerta = f"{self.nomeHospede}, infelizmente a reserva não foi realizada..."
        print(alerta)


if __name__ == "__main__":
    quarto = Quarto(1)
    quarto2 = Quarto(2)

    hospede = Hospede("Thales")
    hospede2 = Hospede("João")

    reserva = Reserva(1)
    reserva2 = Reserva(2)

    reserva.sub(quarto)
    reserva.sub(hospede)
    reserva.realizar_reserva(quarto)

    reserva2.sub(quarto2)
    reserva2.sub(hospede2)
    reserva2.realizar_reserva(quarto)

        



