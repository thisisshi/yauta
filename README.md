## yauta - TeslaAPI
'yet another unofficial tesla api'

Yauta is another implementation of the Tesla Owner API's, with great help
coming from timdorr's documentation which can be found
[here](https://tesla-api.timdorr.com/).

This is a python implementation of the apis, as the few python versions I've
found across the internet either have dubious security practices (e.g. downloading
client id/secret directly from pastebin) or implement the api in such a way
that requires the api consumer to have a somewhat high amount of familiarity
with the api's-- requiring users to know the paths where the apis reside.


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
from yauta.tesla import TeslaAPI


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

## TODO:
- finish implementing rest of api interface for vehicle
- add tests
- add docs crediting unofficial api
- create config file
- create cli
```shell
# example commands
$ yauta init --email $TESLA_EMAIL --password $TESLA_PASSWORD
$ yauta get-access-token --email $TESLA_EMAIL --password $TESLA_PASSWORD
$ yauta set-access-token $TESLA_ACCESS_TOKEN
$ yauta get-vehicles
$ yauta vehicles get-details --vehicle $vehicle_id
$ yauta vehicles honk-horn --vehicle vehicle_id 
$ yauta vehicles wake-up --vehicle $vehicle_id
```
- add dashboarding
- build docs
- add license
