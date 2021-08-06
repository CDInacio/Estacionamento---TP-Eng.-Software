import time
import random


class ParkingLot:
    def __init__(self):
        self.__name = 'UFOP PARKING'
        self.__spots = {
            1: 'empty', 2: 'empty', 3: 'empty', 4: 'empty', 5: 'empty', 6: 'empty', 7: 'empty',
            8: 'empty', 9: 'empty', 10: 'empty', 11: 'empty', 12: 'empty', 13: 'empty', 14: 'empty',
            15: 'empty', 16: 'empty', 17: 'empty', 18: 'empty', 19: 'empty', 20: 'empty', 21: 'empty',
            22: 'empty', 23: 'empty', 24: 'empty', 25: 'empty', 26: 'empty', 27: 'empty', 28: 'empty',
            29: 'empty', 30: 'occupied', 31: 'empty', 32: 'empty', 33: 'empty', 34: 'empty', 35: 'empty',
            36: 'empty', 37: 'empty', 38: 'empty', 39: 'occupied', 40: 'empty', 41: 'empty', 42: 'empty',
            43: 'empty', 44: 'empty', 45: 'empty', 46: 'empty', 47: 'empty', 48: 'empty', 49: 'empty', 50: 'empty'
        }
        self.__client_info = {}
        self.num_clientes = 0


    @property
    def name(self):
        return self.__name


    @property
    def spots(self):
        return self.__spots


    @property
    def client_info(self):
        return self.__client_info


    @staticmethod
    def generate_ticket():
        ticket = random.randint(0, 1000)
        return ticket


    def greetings(self, costumer_name, costumer_spot):
        print(f'SEJA BEM-VINDO AO {self.name}, {costumer_name}.')
        print('Nossos precos sao calculados com base no tempo estacionado.')
        print('A cada hora estacionado lhe sera combrado um valor de R$ 10,00.')
        print(f'Seu carro pode ser estacionado na vaga {costumer_spot}.')


    def park_car(self, plate_number, name):
        print('ESTACIONANDO O CARRO...\n')
        costumer_spot = 0
        # cont = 0
        for key, value in self.spots.items():
            if value == 'empty':
                # cont += 1
                self.spots[key] = 'occupied'
                costumer_spot = key
                break
        # print(f'vagas disponiveis: {cont}')
        self.num_clientes += 1
        self.store_costumer_info(plate_number, name, costumer_spot)
        return costumer_spot


    def store_costumer_info(self, plate_number, name, car_spot):
        self.client_info['name'] = name
        self.client_info['plate_number'] = plate_number
        self.client_info['car_spot'] = car_spot
        self.client_info[''] = car_spot


    def unpark_car(self, costumer_spot):
        print('REMOVENDO O CARRO...')
        self.spots[costumer_spot] = 'empty'
        del self.client_info['name']
        del self.client_info['plate_number']
        del self.client_info['car_spot']


    @staticmethod
    def bill_generate(time):
        # tempo em minutos
        price = time * 10
        print(f'Seu carro ficou estacionado por : {time:.2f} horas, sua conta deu um total de R$: {price:.2f}\n\n')


if __name__ == '__main__':
    pass
