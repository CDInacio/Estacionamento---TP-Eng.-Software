from datetime import date, datetime
from math import e
from parking_lot import *
from random import sample
import time

start = datetime.now()
time.sleep(5)
end = datetime.now()

res = end - start
ParkingLot.bill_generate(start, end)
print(type(res.total_seconds()))