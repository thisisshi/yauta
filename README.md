## nikola - TeslaAPI
hacking on cars


## Installation
Ensure that you have python3 and virtualenv installed on your machine. Then,
simply use the Makefile to install:

```shell
$ make install
```

## Removal

```shell
$ make clean
```

## Usage

Set the following environment variables to allow the sdk to reach out to
Tesla's API:

- `TESLA_EMAIL`: the email address of your Tesla account
- `TESLA_PASSWORD`: the password to your Tesla account
- `TESLA_CLIENT_ID`: client id for the API
- `TESLA_CLIENT_SECRET`: client secret for the API

Tesla's client id and secret can be found with a cursory google search

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

t.initialize()

vehicles = t.get_vehicles()
my_car = vehicles[0]

my_car.wake()

# vehicle data can only be pulled when the vehicle is "online"
time.sleep(90)

data = my_car.get_vehicle_data()
pprint.pprint(data)
```
