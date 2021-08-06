import time
import random
random_time = random.randint(3600, 18000)
rand_time = round((random_time/3600), 2)

from parking_lot import ParkingLot
from client import Client


ufop_parking = ParkingLot()
client_1 = Client('Claudio Dantas', 'RIO2A18')
client_2 = Client('Guilherme Sei la Oq', 'RIO2A20')
client_3 = Client('Rafael Nepomuceno', 'RIO2A98')

##### CLIENTE 1 #####
#  um ticket é gerado quando o cliente chega para estacionar
ticket = ufop_parking.generate_ticket()

# o cliente estaciona o carro
arrival = time.time()
costumer_spot = ufop_parking.park_car(client_1.plate_number, client_1.name)
ufop_parking.greetings(client_1.name, costumer_spot)

# cliente recebe um código de verificação ao estacionar
# client_1.add_verification_ticket(ticket)

# cliente tira o carro do estacionamento    
ufop_parking.unpark_car(costumer_spot)
departure = time.time()
total_time = (departure - arrival) + rand_time

# um valor é gerado para o cliente pagar
ufop_parking.bill_generate(total_time)


##### CLIENTE 2 #####
#  um ticket é gerado quando o cliente chega para estacionar
ticket = ufop_parking.generate_ticket()

# o cliente estaciona o carro
arrival = time.time()
costumer_spot = ufop_parking.park_car(client_2.plate_number, client_2.name)
ufop_parking.greetings(client_2.name, costumer_spot)

# cliente recebe um código de verificação ao estacionar
# client_1.add_verification_ticket(ticket)

# cliente tira o carro do estacionamento    
ufop_parking.unpark_car(costumer_spot)
departure = time.time()
total_time = (departure - arrival) + rand_time

# um valor é gerado para o cliente pagar
ufop_parking.bill_generate(total_time)










