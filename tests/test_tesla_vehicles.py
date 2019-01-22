import os
from unittest import TestCase

from yauta.tesla import TeslaAPI
from yauta.vehicle import TeslaVehicle

from .common import yauta_vcr


class TeslaVehicleTest(TestCase):
    @yauta_vcr.use_cassette('test_tesla_get_vehicle_details_by_id')
    def test_get_tesla_vehicle_details_by_id(self):
        vehicle_id = 'xxxxxxxx'
        access_token = os.environ.get('TESLA_ACCESS_TOKEN', 'xxxxxxxx')
        t = TeslaAPI(
           email='xxxxxxxx',
           password='xxxxxxxx',
           client_id='xxxxxxxx',
           client_secret='xxxxxxxx'
        )
        t.initialize(access_token=access_token)
        vehicle = TeslaVehicle(vehicle_id, t)
        data = vehicle.get_vehicle_data()
        self.assertTrue(data)
