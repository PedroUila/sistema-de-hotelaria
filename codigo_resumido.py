from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import os

def lipar_terminal():
    input()
    os.system('cls')


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
        self.reserva_num_quarto: int
        self.reserva_nome_hospede: str
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
            alerta = f"O quarto {self.numQuarto} foi reservado!"
        else: 
            alerta = f"O quarto {self.numQuarto} já está ocupado!"
        print(alerta)
    
    def __str__(self) -> str:
        return f"Nº quarto: {self.numQuarto}"

class Hospede(Observador):
    def __init__(self, nomeHospede):
        self.nomeHospede = nomeHospede

    def update(self, reserva: Reserva):
        if reserva.reserva_realizada:
            alerta = f"{self.nomeHospede}, a reserva foi realizada com sucesso!"
        else:
            alerta = f"{self.nomeHospede}, infelizmente a reserva não foi realizada..."
        print(alerta)

    def __str__(self) -> str:
        return f"Nome: {self.nomeHospede}"

if __name__ == "__main__":
    lista_de_quartos: list[Quarto] = []
    lista_de_reserva: list[Reserva] = []
    lista_de_quartos.append(Quarto(1))
    lista_de_quartos.append(Quarto(2))
    lista_de_quartos.append(Quarto(3))
    lista_de_quartos.append(Quarto(4))

    numReserva = 1

    while True:
        print("=-= Quartos do hotel =-=")
        for quarto in lista_de_quartos:
            situacao_disponibilidade = "✅" if quarto.disponivel else "❌"
            print(f"Quarto Nº {quarto.numQuarto} {situacao_disponibilidade}")
        print()

        nome_do_hospede = input("Informe o seu nome: ")
        numero_do_quarto = int(input("Informe o quarto que deseja reservar: "))
        if numero_do_quarto == 0:
            break          
        
        quarto_escolhido = lista_de_quartos[numero_do_quarto - 1]
        hospede = Hospede(nome_do_hospede)
        reserva = Reserva(numReserva)
        reserva.sub(hospede)
        reserva.sub(quarto_escolhido)
        reserva.realizar_reserva(quarto_escolhido)
        if reserva.reserva_realizada:
            lista_de_reserva.append(reserva)
            numReserva += 1
        lipar_terminal()

    for reserva in lista_de_reserva:
        print(f"=-= Reserva Nº {reserva.id_reserva} =-=")
        for observer in reserva.lista_observadores:
            print(f"{observer}")
        



