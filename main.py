import time

from parking_lot import ParkingLot
from client import Client


ufop_parking = ParkingLot()
client_1 = Client('Thomas Turbano', 'RIO2A18')

client_name = client_1.name

ufop_parking.greetings(client_name)

ticket = ufop_parking.generate_ticket()

ufop_parking.park_car(ticket)

client_1.add_verification_ticket(ticket)