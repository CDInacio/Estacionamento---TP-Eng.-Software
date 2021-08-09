from datetime import datetime
import time

from parking_lot import *
from client import *


ufop_parking = ParkingLot()
client_1 = Client('Cludio Dantas', 'RIO2A17')
client_2 = Client('Vitor Dantas', 'RIO2A18')


### CLIENTE 1 ###
ufop_parking.greetings()

start = datetime.now()

spot = ufop_parking.park_car(client_1.plate_number)

time.sleep(5)

ufop_parking.store_costumer_info(client_1.plate_number, spot)

ufop_parking.generate_ticket(start, spot)

ufop_parking.unpark_car(spot)

end = datetime.now()

ufop_parking.bill_generate(start, end, spot)

