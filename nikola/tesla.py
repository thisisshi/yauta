from requests import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


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
            status_forcelist=[ 502, 503, 504 ]
        )
        self.mount('https://', HTTPAdapter(max_retries=retries))
        self.headers.update(self._get_access_token())

    def get(self, url, *args, **kwargs):
        url = self.prefix_url + url
        return super(TeslaAPI, self).get(url, *args, **kwargs)

    def post(self, url, *args, **kwargs):
        url = self.prefix_url + url
        return super(TeslaAPI, self).post(url, *args, **kwargs)

    def patch(self, url, *args, **kwargs):
        url = self.prefix_url + url
        return super(TeslaAPI, self).patch(url, *args, **kwargs)

    def _get_access_token(self):
        oauth_url = '/oauth/token?grant_type=password'
        payload = {
            'grant_type': 'password',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'email': self.email,
            'password': self.password
        }
        resp = self.post(oauth_url, data=payload).json()
        return {'Authorization': 'Bearer %s' % resp['access_token']}


    def get_vehicles(self):
        """
        Returns list of all vehicles

        input:
        None
        """
        vehicles_url = '/api/1/vehicles'
        vehicles = self.get(vehicles_url).json()['response']
        vehicle_list = [TeslaVehicle(v, self) for v in vehicles]
        return vehicle_list

    def get_vehicle_data(self, vehicle_id):
        """
        Returns vehicle data

        input:
        vehicle_id: (str) vehicle id number from tesla
        """
        vehicle_data_url = '/api/1/vehicles/%s/vehicle_data' % vehicle_id
        return self.get(vehicle_data_url).json()['response']



class TeslaVehicle(object):
    def __init__(self, vehicle, api):
        self.id = vehicle['id']
        self.vehicle_id = vehicle['vehicle_id']
        self.vin = vehicle['vin']
        self.display_name = vehicle['display_name']
        self.option_codes = vehicle['option_codes'] # TODO: turn this into an array
        self.color = vehicle['color']
        self.state = vehicle['state']
        self.in_service = vehicle['in_service']
        self.calendar_enabled = vehicle['calendar_enabled']
        self.api_version = vehicle['api_version']

        self.api = api
        self.api.prefix_url = self.api.prefix_url + '/api/1/vehicles/%s' % self.id

    def get_vehicle_data(self):
        vehicle_data_url = '/vehicle_data'
        return self.api.get(vehicle_data_url).json()['response']

    def wake_up(self):
        wake_url = '/wake_up'
        return self.api.post(wake_url).json()['response']

    def honk_horn(self):
        pass

    def flash_lights(self):
        pass

    def remote_start_drive(self):
        pass

    def speed_limit_set_limit(self, limit):
        """
        input
        limit: (int) speed limit in mph, must be between 50 and 90
        """
        pass

    def speed_limit_activate(self, pin):
        """
        input
        pin: (str) existing pin if previously set or a new pin
        """
        pass

    def speed_limit_deactivate(self, pin):
        """
        input
        pin: (str) pin to deactivate speed limit
        """
        pass

    def speed_limit_clear_pin(self, pin):
        """
        input
        pin: (str) pin used when activating speed limit
        """
        pass

    def set_valet_mode(self, state, pin):
        """
        input
        state: (bool) true to activate, false to deactivate
        pin: (str) pin to deactivate valet mode
        """
        pass

    def reset_valet_pin(self):
        pass

    def door_unlock(self):
        pass

    def door_lock(self):
        pass

    def actuate_trunk(self, position):
        """
        input:
        position: (str) either `front` or `rear`
        """
        pass

    def sun_roof_control(self, state):
        """
        input:
        state: (str) either `vent` or `close`
        """
        pass

    def charge_port_door_open(self):
        pass

    def charge_port_door_close(self):
        pass

    def charge_start(self):
        pass

    def charge_stop(self):
        pass

    def charge_standard(self):
        pass

    def charge_max_range(self):
        pass

    def set_charge_limit(self, percent):
        """
        input
        percent: (int) ther percentage the battery will be
        charged until must be between 10 and 100
        """
        pass

    def auto_conditioning_start(self):
        pass

    def auto_conditioning_stop(self):
        pass

    def set_temps(self, driver_temp, passenger_temp):
        """
        input
        driver_temp: (long) desired temp on driver's side in celsius
        passenger_temp: (long) desired temp on driver's side in celsius
        """
        pass

    def remote_seat_heater_request(self, heater, level):
        """
        input
        heater: (int) desired seat to heat (0-4)
        level: (int) desired level for heater (0-3)
        """
        pass


    def media_toggle_playback(self):
        pass

    def media_next_track(self):
        pass

    def media_prev_track(self):
        pass

    def media_next_fav(self):
        pass

    def media_prev_fav(self):
        pass

    def media_volume_up(self):
        pass

    def media_volume_down(self):
        pass

    def navigation_request(self, locale, value):
        """
        input
        locale: (str) the locale for the navigation request
        value: (str) the address to set as the destination
        """
        pass

    def schedule_software_update(self, offset_sec):
        """
        input
        offset_sec: (int) number of seconds in the future
        to schedule the software update
        """
        pass

    def cancel_software_update(self):
        pass
