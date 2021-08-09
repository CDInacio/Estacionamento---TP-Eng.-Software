import time
from datetime import datetime

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
    time.sleep(2)
    ufop_parking.store_costumer_info(client_1.plate_number, car_spot)
    ufop_parking.unpark_car(car_spot)
    end = datetime.now()
    ufop_parking.bill_generate(start, end)
    
    
spot = ufop_parking.check_vacancy()
time.sleep(2)
if spot == 0:
    print('Nao ha vagas disponiveis no momento!')
else:
    start = datetime.now()
    car_spot = ufop_parking.park_car(client_2.plate_number)
    print('Gerando ticket...')
    time.sleep(1)
    ticket = ufop_parking.generate_ticket(start, car_spot)
    print('Ticket gerado...')
    time.sleep(2)
    ufop_parking.store_costumer_info(client_2.plate_number, car_spot)
    ufop_parking.unpark_car(car_spot)
    end = datetime.now()
    ufop_parking.bill_generate(start, end)









