import os

from unittest import TestCase

from yauta.tesla import TeslaAPI
from yauta.vehicle import TeslaVehicle

from .common import yauta_vcr


class TeslaTest(TestCase):
    @yauta_vcr.use_cassette('test_tesla_get_auth_with_email.yml')
    def test_get_tesla_auth(self):
        email = os.environ.get('TESLA_EMAIL')
        password = os.environ.get('TESLA_PASSWORD')
        client_id = os.environ.get('TESLA_CLIENT_ID')
        client_secret = os.environ.get('TESLA_CLIENT_SECRET')
        t = TeslaAPI(
            email=email,
            password=password,
            client_id=client_id,
            client_secret=client_secret
        )

        t.initialize()
        self.assertTrue(t.headers['Authorization'])

    def test_initialize_tesla_with_access_token(self):
        t = TeslaAPI(
            email='xxxxxxx',
            password='xxxxxxx',
            client_id='xxxxxxxx',
            client_secret='xxxxxxxx'
        )
        t.initialize('XXXXXXXXXXX')
        self.assertTrue(t.access_token)
        self.assertEqual(t.access_token, 'XXXXXXXXXXX')
        self.assertTrue(t.headers['Authorization'])
        self.assertEqual(t.headers['Authorization'], 'Bearer XXXXXXXXXXX')

    @yauta_vcr.use_cassette('test_tesla_get_vehicles.yml')
    def test_get_tesla_vehicles(self):
        access_token = os.environ.get('TESLA_ACCESS_TOKEN', 'xxxxxxxx')
        t = TeslaAPI(
            email='xxxxxxx',
            password='xxxxxxx',
            client_id='xxxxxxxx',
            client_secret='xxxxxxxx'
        )
        t.initialize(access_token=access_token)
        vehicles = t.get_vehicles()
        self.assertEqual(len(vehicles), 1)

        self.assertTrue(isinstance(vehicles[0], TeslaVehicle))
