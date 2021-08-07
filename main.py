import time
import random
from datetime import datetime

random_time = random.randint(3600, 18000)
rand_time = round((random_time/3600), 2)

from parking_lot import ParkingLot
from client import Client


ufop_parking = ParkingLot()
client_1 = Client('Claudio Dantas', 'RIO2A18')
client_2 = Client('Guilherme Sei la Oq', 'RIO2A20')
client_3 = Client('Rafael Nepomuceno', 'RIO2A98')


ufop_parking.greetings()
spot = ufop_parking.check_vacancy()

time.sleep(2)

if spot == 0:
    print('Nao ha vagas disponiveis no momento!')
else:
    start = datetime.now()
    car_spot = ufop_parking.park_car(client_1.plate_number)
    print('Gerando ticket...')
    time.sleep(1)
    ticket = ufop_parking.generate_ticket(start, car_spot)
    print('Ticket gerado...')
    time.sleep(10)
    ufop_parking.store_costumer_info(client_1.plate_number, car_spot)
    ufop_parking.unpark_car(car_spot)
    end = datetime.now()
    ufop_parking.bill_generate(start, end)









