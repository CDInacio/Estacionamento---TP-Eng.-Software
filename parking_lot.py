import time
import random
from datetime import datetime

class ParkingLot:
    def __init__(self):
        self.__name = 'UFOP PARKING'
        self.__spots = {
            1: 'occupied', 2: 'occupied', 3: 'occupied', 4: 'occupied', 5: 'empty', 6: 'empty', 7: 'empty',
            8: 'empty', 9: 'empty', 10: 'empty', 11: 'occupied', 12: 'empty', 13: 'empty', 14: 'empty',
            15: 'empty', 16: 'empty', 17: 'empty', 18: 'empty', 19: 'empty', 20: 'empty', 21: 'empty',
            22: 'empty', 23: 'empty', 24: 'occupied', 25: 'empty', 26: 'empty', 27: 'empty', 28: 'empty',
            29: 'empty', 30: 'occupied', 31: 'empty', 32: 'empty', 33: 'empty', 34: 'empty', 35: 'empty',
            36: 'empty', 37: 'empty', 38: 'empty', 39: 'occupied', 40: 'empty', 41: 'empty', 42: 'empty',
            43: 'empty', 44: 'empty', 45: 'empty', 46: 'empty', 47: 'empty', 48: 'empty', 49: 'empty', 
            50: 'empty'
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
    def generate_ticket(time, spot):
        ticket_info = dict()
        num = random.randint(0, 1000)
        ticket_info['num'] = num
        ticket_info['arrival'] = time.strftime("%H:%M:%S")
        ticket_info['car_spot'] = spot
        return ticket_info


    def check_vacancy(self):
        cont = 0
        for key, value in self.spots.items():
            if value == 'empty':
                cont += 1
        return cont
            
            
    @staticmethod
    def greetings():
        print(f'##### SEJA BEM-VINDO AO UFOP PARKING!! #####')
        print('Nossos precos sao calculados com base no tempo estacionado.')
        print('A cada hora estacionado lhe sera combrado um valor de R$ 10,00.')
        print('Aguarde enquanto verificamos se ha vagas disponiveis')


    def park_car(self, plate_number):
        num = self.check_vacancy()
        if num == 0:
            print('Nao ha vagas')
            return
            
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
        self.store_costumer_info(plate_number, costumer_spot)
        return costumer_spot


    def store_costumer_info(self, plate_number, car_spot):
        if car_spot == None:
            return
        self.client_info['plate_number'] = plate_number
        self.client_info['car_spot'] = car_spot
        self.client_info[''] = car_spot


    def unpark_car(self, costumer_spot):
        if costumer_spot == None:
            return
        print('REMOVENDO O CARRO...')
        self.spots[costumer_spot] = 'empty'
        del self.client_info['plate_number']
        del self.client_info['car_spot']


    @staticmethod
    def bill_generate(start, end, car_spot):
        if car_spot == None:
            return
        # tempo em minutos
        time = end - start
        sub_time = time.total_seconds()
        price = ((sub_time)/3600) * 10
        print(f'Seu carro ficou estacionado por : {(sub_time/60):.2f} horas, sua conta deu um total de R$: {price:.2f}\n\n')



if __name__ == '__main__':
    pass
