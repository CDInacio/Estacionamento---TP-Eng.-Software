import time
import random

class ParkingLot:
    def __init__(self):
        self.__name = 'UFOP Parking'
        self.__spots = {
            1: 'empty', 2: 'empty', 3: 'empty', 4: 'empty', 5: 'empty', 6: 'empty', 7: 'empty',
            8: 'empty', 9: 'empty', 10: 'empty',11: 'empty', 12: 'empty', 13: 'empty', 14: 'empty',
            15: 'empty', 16: 'empty', 17: 'empty', 18: 'empty', 19: 'empty', 20: 'empty',21: 'empty',
            22: 'empty', 23: 'empty', 24: 'empty', 25: 'empty', 26: 'empty', 27: 'empty', 28: 'empty',
            29: 'empty', 30: 'occupied',31: 'empty', 32: 'empty', 33: 'empty', 34: 'empty', 35: 'empty',
            36: 'empty', 37: 'empty', 38: 'empty', 39: 'occupied', 40: 'empty', 41: 'empty', 42: 'empty',
            43: 'empty', 44: 'empty', 45: 'empty', 46: 'empty', 47: 'empty', 48: 'empty', 49: 'empty', 50: 'empty'
        }
        self.__client_plate_number = []


    @property
    def name(self):
        return self.__name


    @property
    def spots(self):
        return self.__spots
    
    
    @property
    def client_plate_number(self):
        return self.__client_plate_number
    

    @staticmethod
    def generate_ticket():
        ticket = random.randint(0, 1000)
        return ticket


    def greetings(self, costumer_name):
        print(f'Ola {costumer_name}, seja bem-vindo ao {self.name}, nossos precos sao calculados com base no tempo estacionado.')
        print('A cada meia hora estacionado sera combrado um valor de R$ 5,00.')
        print('Um ticket lhe sera entregue como forma de controle de clientes. \n Em caso de perda do mesmo, a placa do seu carro sera usada como ticket\n')


    def unpark_car(self, costumer_spot):
        for key, value in self.spots.items():
            self.spots[costumer_spot] = 'empty'


    def park_car(self, ticket):
        costumer_spot = 0
        # cont = 0
        for key, value in self.spots.items():
            if value == 'empty':
                # cont += 1
                self.spots[key] = 'occupied'
                costumer_spot = key
                break
        # print(f'vagas disponiveis: {cont}') 
        print(f'Seu carro sera estacionado na vaga: {costumer_spot}, e seu ticket de indentificacao eh: {ticket}')

        
    
    def get_costumer_plate_number(self, plate_number):
        self.client_plate_number.append(plate_number)
        

if __name__ == '__main__':
    pass
