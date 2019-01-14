## TeslaAPI
hacking on cars

```python
import os
import time
import pprint
from nikola.tesla import TeslaAPI


t = TeslaAPI(
   email=os.environ.get('TESLA_EMAIL'),
   password=os.environ.get('TESLA_PASSWORD'),
   client_id=os.environ.get('TESLA_CLIENT_ID'),
   client_secret=os.environ.get('TESLA_CLIENT_SECRET')
)

vehicles = t.get_vehicles()
my_car = vehicles[0]

my_car.wake()

# vehicle data can only be pulled when the vehicle is "online"
time.sleep(90)

data = my_car.get_vehicle_data()
pprint.pprint(data)
```
