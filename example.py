import os
import pprint
import time
from yauta.tesla import TeslaAPI


t = TeslaAPI(
   email=os.environ.get('TESLA_EMAIL'),
   password=os.environ.get('TESLA_PASSWORD'),
   client_id=os.environ.get('TESLA_CLIENT_ID'),
   client_secret=os.environ.get('TESLA_CLIENT_SECRET')
)

access_token = os.environ.get('TESLA_ACCESS_TOKEN')

if access_token:
    t.initialize(access_token=access_token)
else:
    t.initialize()

vehicles = t.get_vehicles()
print('Got %s vehicles' % len(vehicles))

my_car = vehicles[0]
print('Car: %s' % my_car.id)

print('Waking up car...')
resp = my_car.wake_up()
my_car.honk_horn()
pprint.pprint(resp)

time.sleep(30)

my_car.get_vehicle_data()
time.sleep(5)
data = my_car.get_vehicle_data()
pprint.pprint(data)
