from requests import Session, HTTPError
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from yauta.exceptions import TeslaAuthException
from yauta.vehicle import TeslaVehicle


class TeslaAPI(Session):

    BASE_URL = 'https://owner-api.teslamotors.com'

    def __init__(self, client_id, client_secret, email, password):
        self.prefix_url = TeslaAPI.BASE_URL
        super(TeslaAPI, self).__init__()

        self.client_id = client_id
        self.client_secret = client_secret
        self.email = email
        self.password = password
        retries = Retry(
            total=5,
            backoff_factor=1,
            status_forcelist=[408, 502, 503, 504]
        )
        self.mount('https://', HTTPAdapter(max_retries=retries))

    def initialize(self, access_token=None):
        try:
            self.headers.update(self._get_access_token(access_token))
        except HTTPError as e:
            raise TeslaAuthException(
                'Unable to initialize, token fetch failed: %s' % e
            )
        return self

    def get(self, url, *args, **kwargs):
        url = self.prefix_url + url
        return super(TeslaAPI, self).get(url, *args, **kwargs)

    def post(self, url, *args, **kwargs):
        url = self.prefix_url + url
        return super(TeslaAPI, self).post(url, *args, **kwargs)

    def patch(self, url, *args, **kwargs):
        url = self.prefix_url + url
        return super(TeslaAPI, self).patch(url, *args, **kwargs)

    def _get_access_token(self, access_token=None):
        if not access_token:
            oauth_url = '/oauth/token?grant_type=password'
            payload = {
                'grant_type': 'password',
                'client_id': self.client_id,
                'client_secret': self.client_secret,
                'email': self.email,
                'password': self.password
            }
            resp = self.post(oauth_url, data=payload)
            resp.raise_for_status()
            access_token = resp.json()['access_token']
        return {'Authorization': 'Bearer %s' % access_token}

    def get_vehicles(self):
        """
        Returns list of all vehicles

        input:
        None

        returns:
        list of TeslaVehicle objects
        """
        vehicles_url = '/api/1/vehicles'
        vehicles = self.get(vehicles_url).json()['response']
        vehicle_list = [TeslaVehicle(v['id'], self) for v in vehicles]
        return vehicle_list
