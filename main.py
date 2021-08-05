import time

from parking_lot import ParkingLot
from client import Client


ufop_parking = ParkingLot()
client_1 = Client('Cláudio Dantas', 'RIO2A18')
client_2 = Client('Guilherme Sei la Oq', 'RIO2A20')
client_3 = Client('Rafael Nepomuceno', 'RIO2A98')

# cliente 1
ufop_parking.greetings(client_1.name)

ticket = ufop_parking.generate_ticket()

res = ufop_parking.park_car(ticket, client_1.plate_number)

# print(ufop_parking.client_plate_number)

client_1.add_verification_ticket(ticket)
print(ufop_parking.spots[1])

